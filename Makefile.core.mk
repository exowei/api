# Copyright Istio Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

all: gen

########################
# setup
########################

repo_dir := .
out_path = /tmp

protoc = protoc -Icommon-protos -I.
protolock = protolock
protolock_release = /bin/bash scripts/check-release-locks.sh
prototool = prototool
annotations_prep = annotations_prep
htmlproofer = htmlproofer

go_plugin_prefix := --go_out=plugins=grpc,
go_plugin := $(go_plugin_prefix):$(out_path)

########################
# protoc_gen_gogo*
########################

gogofast_plugin_prefix := --gogofast_out=plugins=grpc,
gogoslick_plugin_prefix := --gogoslick_out=plugins=grpc,

comma := ,
empty :=
space := $(empty) $(empty)

importmaps := \
	gogoproto/gogo.proto=github.com/gogo/protobuf/gogoproto \
	google/protobuf/any.proto=github.com/gogo/protobuf/types \
	google/protobuf/descriptor.proto=github.com/gogo/protobuf/protoc-gen-gogo/descriptor \
	google/protobuf/duration.proto=github.com/gogo/protobuf/types \
	google/protobuf/struct.proto=github.com/gogo/protobuf/types \
	google/protobuf/timestamp.proto=github.com/gogo/protobuf/types \
	google/protobuf/wrappers.proto=github.com/gogo/protobuf/types \
	google/rpc/status.proto=exowei.io/gogo-genproto/googleapis/google/rpc \
	google/rpc/code.proto=exowei.io/gogo-genproto/googleapis/google/rpc \
	google/rpc/error_details.proto=exowei.io/gogo-genproto/googleapis/google/rpc \
	google/api/field_behavior.proto=exowei.io/gogo-genproto/googleapis/google/api \

# generate mapping directive with M<proto>:<go pkg>, format for each proto file
mapping_with_spaces := $(foreach map,$(importmaps),M$(map),)
gogo_mapping := $(subst $(space),$(empty),$(mapping_with_spaces))

gogofast_plugin := $(gogofast_plugin_prefix)$(gogo_mapping):$(out_path)
gogoslick_plugin := $(gogoslick_plugin_prefix)$(gogo_mapping):$(out_path)

########################
# protoc_gen_python
########################

python_output_path := python/exowei_api
protoc_gen_python_prefix := --python_out=,
protoc_gen_python_plugin := $(protoc_gen_python_prefix):$(repo_dir)/$(python_output_path)

########################
# protoc_gen_docs
########################

protoc_gen_docs_plugin := --docs_out=warnings=true,dictionary=$(repo_dir)/dictionaries/en-US,custom_word_list=$(repo_dir)/dictionaries/custom.txt,mode=html_fragment_with_front_matter:$(repo_dir)/
protoc_gen_docs_plugin_per_file := --docs_out=warnings=true,dictionary=$(repo_dir)/dictionaries/en-US,custom_word_list=$(repo_dir)/dictionaries/custom.txt,per_file=true,mode=html_fragment_with_front_matter:$(repo_dir)/

########################
# protoc_gen_jsonshim
########################

protoc_gen_k8s_support_plugins := --jsonshim_out=$(gogo_mapping):$(out_path) --deepcopy_out=$(gogo_mapping):$(out_path)

#####################
# Generation Rules
#####################

gen: \
	generate-ethereum \
	tidy-go \
	mirror-licenses \

gen-check: clean gen check-clean-repo

#####################
# ethereum/...
#####################

ethereum_v1alpha1_path := ethereum/v1alpha1
ethereum_v1alpha1_protos := $(wildcard $(ethereum_v1alpha1_path)/*.proto)
ethereum_v1alpha1_pb_gos := $(ethereum_v1alpha1_protos:.proto=.pb.go)
ethereum_v1alpha1_pb_pythons := $(patsubst $(ethereum_v1alpha1_path)/%.proto,$(python_output_path)/$(ethereum_v1alpha1_path)/%_pb2.py,$(ethereum_v1alpha1_protos))
ethereum_v1alpha1_pb_docs := $(ethereum_v1alpha1_protos:.proto=.pb.html)

$(ethereum_v1alpha1_pb_gos) $(ethereum_v1alpha1_pb_docs) $(ethereum_v1alpha1_pb_pythons): $(ethereum_v1alpha1_protos)
	@$(protolock) status
	@$(protoc) $(gogofast_plugin)  $(protoc_gen_python_plugin) $(protoc_gen_docs_plugin)$(ethereum_v1alpha1_path) $^
	@cp -r /tmp/exowei.io/api/ethereum/* ethereum

generate-ethereum: $(ethereum_v1alpha1_pb_gos) $(ethereum_v1alpha1_pb_docs) $(ethereum_v1alpha1_pb_pythons)

clean-ethereum:
	@rm -fr $(ethereum_v1alpha1_pb_gos) $(ethereum_v1alpha1_pb_docs) $(ethereum_v1alpha1_pb_pythons)

#####################
# Protolock
#####################

proto-commit:
	@$(protolock) commit

proto-commit-force:
	@$(protolock) commit --force

proto-status:
	@$(protolock) status

release-lock-status:
	@$(protolock_release)

#####################
# Misc
#####################

lint: lint-all
 	@$(htmlproofer) . --url-swap "exowei.io:preliminary.exowei.io" --assume-extension --check-html --check-external-hash --check-opengraph --timeframe 2d --storage-dir $(repo_dir)/.htmlproofer --url-ignore "/localhost/"

fmt: format-python

#####################
# Cleanup
#####################

clean: \
	clean-ethereum

#####################
# CI System
#####################

presubmit: proto-commit lint release-lock-status
postsubmit: presubmit

#####################
# Common definitions
#####################

include common/Makefile.common.mk
