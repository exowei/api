# Exowei APIs and Common Configuration Definitions

This repository defines component-level APIs and common configuration formats for the Exowei
platform. These definitions are specified using the [protobuf](https://github.com/google/protobuf)
syntax.

This repository depends only on the [tools](https://github.com/istio/tools) repository for tools used during build. This repository *will not* depend on any
other repositories. Except for tools, all other Exowei repositories can take a dependency on the api repository.

## API Guidelines

When making changes to the protos in this repository, your changes **must** comply with the [API guidelines](./GUIDELINES.md).

## Updating

After the [protobuf](https://github.com/google/protobuf) definitions
are updated, the corresponding `*pb.go`, `_pb2.py`, `*.json` and
Kubernetes Custom Resource Definition files must be
generated by running `make clean gen` and submitted as
part of the same PR as the updated definitions. Also `make
proto-commit` must be run to update the proto.lock file with new
changes.

If releasing a new tagged version, please update python/exowei-api/setup.py version to reflect.

## Backwards Incompatible Changes

If a PR tries to make backwards incompatible changes, it will be
blocked by protolock. To force these changes in, install
[protolock](https://github.com/nilslice/protolock) and run
`protolock commit --force`.

You must include a note in your PR that you had to force the
protolock and why.
