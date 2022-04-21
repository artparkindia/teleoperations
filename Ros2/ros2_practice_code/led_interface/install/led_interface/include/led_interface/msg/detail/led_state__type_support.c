// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from led_interface:msg/LedState.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "led_interface/msg/detail/led_state__rosidl_typesupport_introspection_c.h"
#include "led_interface/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "led_interface/msg/detail/led_state__functions.h"
#include "led_interface/msg/detail/led_state__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void LedState__rosidl_typesupport_introspection_c__LedState_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  led_interface__msg__LedState__init(message_memory);
}

void LedState__rosidl_typesupport_introspection_c__LedState_fini_function(void * message_memory)
{
  led_interface__msg__LedState__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember LedState__rosidl_typesupport_introspection_c__LedState_message_member_array[1] = {
  {
    "state",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(led_interface__msg__LedState, state),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers LedState__rosidl_typesupport_introspection_c__LedState_message_members = {
  "led_interface__msg",  // message namespace
  "LedState",  // message name
  1,  // number of fields
  sizeof(led_interface__msg__LedState),
  LedState__rosidl_typesupport_introspection_c__LedState_message_member_array,  // message members
  LedState__rosidl_typesupport_introspection_c__LedState_init_function,  // function to initialize message memory (memory has to be allocated)
  LedState__rosidl_typesupport_introspection_c__LedState_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t LedState__rosidl_typesupport_introspection_c__LedState_message_type_support_handle = {
  0,
  &LedState__rosidl_typesupport_introspection_c__LedState_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_led_interface
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, led_interface, msg, LedState)() {
  if (!LedState__rosidl_typesupport_introspection_c__LedState_message_type_support_handle.typesupport_identifier) {
    LedState__rosidl_typesupport_introspection_c__LedState_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &LedState__rosidl_typesupport_introspection_c__LedState_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
