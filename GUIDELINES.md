# Exowei API Guidelines

This page defines the design guidelines for Exowei APIs. They apply to
all [proto files](https://developers.google.com/protocol-buffers/).

We will use Google's [API Design Guide](https://cloud.google.com/apis/design) as
the baseline for protos.

In addition to Google's guide, the following conventions should be
followed for Exowei APIs.

## Contents

- [Proto Guidelines](#proto-guidelines)
    - [Style](#style)
    - [Basic Proto Versioning](#basic-proto-ersioning)

## Proto Guidelines

This section captures guidelines that apply to the proto form of the configuration resources.

### Style

#### Placement

- **Do** place new API protos under ```exowei.io/api/<area>/<version>``` folder.
- **Prefer** complete words for file names.

    ```
    index.proto // Not idx.proto!
    ```

#### Package Names

- **Do** use `lowercase` without any `_`.
- **Do** use singular words
- **Do** use the name pattern ```exowei.<area>.<version>```.

    ```proto
    package exowei.networking.v1alpha3;
    ```

#### Message/Enum/Method Names

- **Do not** use embedded acronyms. See [#364](https://github.com/istio/api/issues/364) for details.

    ```proto
    message HttpRequest {/*...*/}  // Not HTTPRequest!

    rpc DoHttpRequest(/*...*/)     // Not DoHTTPRequest!

    enum HttpStatusCodes {/*...*/} // Not HTTPStatusCodes!
    ```

#### Messages

- **Do** use ```CamelCase``` for message names.

    ```proto
    message MyMessage {...}
    ```

#### Fields

- **Do** use ```lowercase_with_underscore``` for field names:

    ```proto
    string display_name = 1;
    ```

- **Do** use plural names for repeated fields:

    ```proto
    repeated rule rules = 2;
    ```

- **Do not** use postpositive adjectives in names.

    ```proto
    repeated Items collected_items = 3; // Not items_collected!
    ```

#### Enums

- **Do** use ```CamelCase``` for  types names.

    ```proto
    enum Types {/*...*/}
    ```

- **Do** use `UPPERCASE_WITH_UNDERSCORE` for enum names:

    ```proto
    enum Types {INT_TYPE = 1;}
    ```

- **Do** have an enum entry for value ```0```.

    - When a new field with an enum type is introduced to a proto, when reading
    the older versions of the data, it will be defaulted to the ```0``` value.

- **Do** name the ```0``` value either as ```<ENUMTYPE>_UNDEFINED``` or use a sane,
well-known value that will be considered as default.

    ```proto
    enum Types { TYPE_UNDEFINED = 0;}
    ```

### Basic Proto Versioning

Protocol Buffers have well-defined semantics for coping with version changes. In essense, the unknown fields
get ignored, and additive, and non-breaking changes are acceptable.

In addition to the standard proto versioning semantics, Exowei tooling imposes its own restrictions, as CRD
to proto conversion system in Exowei depends on names in certain situations.

The following rules captures the basic rules that should be followed when making changes to Exowei config
protos.

- **Do not** change field numbers.

    - Proto depends on field numbers to find fields.

        ```proto
        // Field number has changed from 1 to 2!

        // string field = 1; // Deleted
        string field = 2;
        ```

- **Do not** rename fields.

    - Our tooling automatically maps YAML fields to proto fields.

        ```proto
        // Field name has changed!

        // string old_field = 1;
        string new_field = 1;
        ```

- **Do not** change cardinality of fields.

    ```proto
    // Field cardinality has changed!

    // string should_have_been_plural = 1;
    repeated string should_have_been_plural = 1;
    ```

- **Do not** rename top-level protos that map to CRD config types.

    - Exowei tooling depends on the name of the top-level protos to map CRDs to the matching proto counterparts.

        ```proto
        // Top-level proto name has changed!

        // message Rule {
        message PolicyRule {
            // ...
        }
        ```

- **Avoid** changing/renaming field types.

    - If the field types changes, the new type **must** be structurally equivalent to the old.

        ```proto
        // Field type changed from Boo to Zoo!
        // Boo and Zoo must be structurally equivalent!
        message Foo {
           // Boo boo = 1;
           Zoo boo = 2;
        }
        ```

- **Do not** rename enum names, or change values.

    - Exowei tooling depends on names to convert enums from CRD form to proto.

        ```proto
        enum Types {
           // Enum name has changed!
           // Foo = 1;
           Bar = 1;

           // Enum value has changed!
           // Baz = 2;
           Baz = 3;
        }
        ```
