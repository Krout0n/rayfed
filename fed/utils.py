# Copyright 2022 The RayFed Team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

import jax
import ray

from fed.fed_object import FedObject

logger = logging.getLogger(__name__)


def resolve_dependencies(current_party, current_fed_task_id, *args, **kwargs):
    from fed.barriers import recv

    flattened_args, tree = jax.tree_util.tree_flatten((args, kwargs))
    indexes = []
    resolved = []
    for idx, arg in enumerate(flattened_args):
        if isinstance(arg, FedObject):
            indexes.append(idx)
            if arg.get_party() == current_party:
                logger.debug(f"Insert fed object, arg.party={arg.get_party()}")
                resolved.append(arg.get_ray_object_ref())
            else:
                logger.debug(
                    f'Insert recv_op, arg task id {arg.get_fed_task_id()}, current'
                    'task id {current_fed_task_id}'
                )
                if arg.get_ray_object_ref() is not None:
                    # This code path indicates the ray object is already received in
                    # this party, so there is no need to receive it any longer.
                    received_ray_obj = arg.get_ray_object_ref()
                else:
                    received_ray_obj = recv(
                        current_party, arg.get_fed_task_id(), current_fed_task_id
                    )
                    arg._cache_ray_object_ref(received_ray_obj)
                resolved.append(received_ray_obj)
    if resolved:
        for idx, actual_val in zip(indexes, resolved):
            flattened_args[idx] = actual_val

    resolved_args, resolved_kwargs = jax.tree_util.tree_unflatten(tree, flattened_args)
    return resolved_args, resolved_kwargs


def is_ray_object_refs(objects) -> bool:
    if isinstance(objects, ray.ObjectRef):
        return True

    if isinstance(objects, list):
        for object_ref in objects:
            if not isinstance(object_ref, ray.ObjectRef):
                return False
        return True

    return False


def setup_logger(
    logging_level,
    logging_format,
    date_format,
    log_dir=None,
    party_val=None,
):
    class PartyRecordFilter(logging.Filter):
        def __init__(self, party_val=None) -> None:
            self._party_val = party_val
            super().__init__("PartyRecordFilter")

        def filter(self, record) -> bool:
            if not hasattr(record, "party"):
                record.party = self._party_val
            return True

    logger = logging.getLogger()

    # Remove default handlers otherwise a msg will be printed twice.
    for hdlr in logger.handlers:
        logger.removeHandler(hdlr)

    if type(logging_level) is str:
        logging_level = logging.getLevelName(logging_level.upper())
    logger.setLevel(logging_level)

    _formatter = logging.Formatter(fmt=logging_format, datefmt=date_format)
    _filter = PartyRecordFilter(party_val=party_val)

    _customed_handler = logging.StreamHandler()
    _customed_handler.setFormatter(_formatter)
    _customed_handler.addFilter(_filter)

    logger.addHandler(_customed_handler)


def tls_enabled(tls_config):
    return True if tls_config else False


def load_cert_config(cert_config):
    ca_cert, private_key, cert_chain = None, None, None
    if "ca_cert" in cert_config:
        with open(cert_config["ca_cert"], "rb") as file:
            ca_cert = file.read()
    with open(cert_config["key"], "rb") as file:
        private_key = file.read()
    with open(cert_config["cert"], "rb") as file:
        cert_chain = file.read()

    return ca_cert, private_key, cert_chain


def is_cython(obj):
    """Check if an object is a Cython function or method"""

    # TODO(suo): We could split these into two functions, one for Cython
    # functions and another for Cython methods.
    # TODO(suo): There doesn't appear to be a Cython function 'type' we can
    # check against via isinstance. Please correct me if I'm wrong.
    def check_cython(x):
        return type(x).__name__ == "cython_function_or_method"

    # Check if function or method, respectively
    return check_cython(obj) or (
        hasattr(obj, "__func__") and check_cython(obj.__func__)
    )
