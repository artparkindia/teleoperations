// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from led_interface:srv/SetLed.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "led_interface/srv/detail/set_led__rosidl_typesupport_introspection_c.h"
#include "led_interface/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "led_interface/srv/detail/set_led__functions.h"
#include "led_interface/srv/detail/set_led__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void SetLed_Request__rosidl_typesupport_introspection_c__SetLed_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  led_interface__srv__SetLed_Request__init(message_memory);
}

void SetLed_Request__rosidl_typesupport_introspection_c__SetLed_Request_fini_function(void * message_memory)
{
  led_interface__srv__SetLed_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember SetLed_Request__rosidl_typesupport_introspection_c__SetLed_Request_message_member_array[2] = {
  {
    "led_number",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(led_interface__srv__SetLed_Request, led_number),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "state",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(led_interface__srv__SetLed_Request, state),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers SetLed_Request__rosidl_typesupport_introspection_c__SetLed_Request_message_members = {
  "led_interface__srv",  // message namespace
  "SetLed_Request",  // message name
  2,  // number of fields
  sizeof(led_interface__srv__SetLed_Request),
  SetLed_Request__rosidl_typesupport_introspection_c__SetLed_Request_message_member_array,  // message members
  SetLed_Request__rosidl_typesupport_introspection_c__SetLed_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  SetLed_Request__rosidl_typesupport_introspection_c__SetLed_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t SetLed_Request__rosidl_typesupport_introspection_c__SetLed_Request_message_type_support_handle = {
  0,
  &SetLed_Request__rosidl_typesupport_introspection_c__SetLed_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_led_interface
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, led_interface, srv, SetLed_Request)() {
  if (!SetLed_Request__rosidl_typesupport_introspection_c__SetLed_Request_message_type_support_handle.typesupport_identifier) {
    SetLed_Request__rosidl_typesupport_introspection_c__SetLed_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &SetLed_Request__rosidl_typesupport_introspection_c__SetLed_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "led_interface/srv/detail/set_led__rosidl_typesupport_introspection_c.h"
// already included above
// #include "led_interface/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "led_interface/srv/detail/set_led__functions.h"
// already included above
// #include "led_interface/srv/detail/set_led__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void SetLed_Response__rosidl_typesupport_introspection_c__SetLed_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  led_interface__srv__SetLed_Response__init(message_memory);
}

void SetLed_Response__rosidl_typesupport_introspection_c__SetLed_Response_fini_function(void * message_memory)
{
  led_interface__srv__SetLed_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember SetLed_Response__rosidl_typesupport_introspection_c__SetLed_Response_message_member_array[1] = {
  {
    "success",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(led_interface__srv__SetLed_Response, success),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers SetLed_Response__rosidl_typesupport_introspection_c__SetLed_Response_message_members = {
  "led_interface__srv",  // message namespace
  "SetLed_Response",  // message name
  1,  // number of fields
  sizeof(led_interface__srv__SetLed_Response),
  SetLed_Response__rosidl_typesupport_introspection_c__SetLed_Response_message_member_array,  // message members
  SetLed_Response__rosidl_typesupport_introspection_c__SetLed_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  SetLed_Response__rosidl_typesupport_introspection_c__SetLed_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t SetLed_Response__rosidl_typesupport_introspection_c__SetLed_Response_message_type_support_handle = {
  0,
  &SetLed_Response__rosidl_typesupport_introspection_c__SetLed_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_led_interface
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, led_interface, srv, SetLed_Response)() {
  if (!SetLed_Response__rosidl_typesupport_introspection_c__SetLed_Response_message_type_support_handle.typesupport_identifier) {
    SetLed_Response__rosidl_typesupport_introspection_c__SetLed_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &SetLed_Response__rosidl_typesupport_introspection_c__SetLed_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "led_interface/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "led_interface/srv/detail/set_led__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers led_interface__srv__detail__set_led__rosidl_typesupport_introspection_c__SetLed_service_members = {
  "led_interface__srv",  // service namespace
  "SetLed",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // led_interface__srv__detail__set_led__rosidl_typesupport_introspection_c__SetLed_Request_message_type_support_handle,
  NULL  // response message
  // led_interface__srv__detail__set_led__rosidl_typesupport_introspection_c__SetLed_Response_message_type_support_handle
};

static rosidl_service_type_support_t led_interface__srv__detail__set_led__rosidl_typesupport_introspection_c__SetLed_service_type_support_handle = {
  0,
  &led_interface__srv__detail__set_led__rosidl_typesupport_introspection_c__SetLed_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, led_interface, srv, SetLed_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, led_interface, srv, SetLed_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_led_interface
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, led_interface, srv, SetLed)() {
  if (!led_interface__srv__detail__set_led__rosidl_typesupport_introspection_c__SetLed_service_type_support_handle.typesupport_identifier) {
    led_interface__srv__detail__set_led__rosidl_typesupport_introspection_c__SetLed_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)led_interface__srv__detail__set_led__rosidl_typesupport_introspection_c__SetLed_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, led_interface, srv, SetLed_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, led_interface, srv, SetLed_Response)()->data;
  }

  return &led_interface__srv__detail__set_led__rosidl_typesupport_introspection_c__SetLed_service_type_support_handle;
}
