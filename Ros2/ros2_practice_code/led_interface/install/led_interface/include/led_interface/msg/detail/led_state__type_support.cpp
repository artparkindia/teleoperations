// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from led_interface:msg/LedState.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "led_interface/msg/detail/led_state__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace led_interface
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void LedState_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) led_interface::msg::LedState(_init);
}

void LedState_fini_function(void * message_memory)
{
  auto typed_message = static_cast<led_interface::msg::LedState *>(message_memory);
  typed_message->~LedState();
}

size_t size_function__LedState__state(const void * untyped_member)
{
  (void)untyped_member;
  return 3;
}

const void * get_const_function__LedState__state(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<int16_t, 3> *>(untyped_member);
  return &member[index];
}

void * get_function__LedState__state(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<int16_t, 3> *>(untyped_member);
  return &member[index];
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember LedState_message_member_array[1] = {
  {
    "state",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(led_interface::msg::LedState, state),  // bytes offset in struct
    nullptr,  // default value
    size_function__LedState__state,  // size() function pointer
    get_const_function__LedState__state,  // get_const(index) function pointer
    get_function__LedState__state,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers LedState_message_members = {
  "led_interface::msg",  // message namespace
  "LedState",  // message name
  1,  // number of fields
  sizeof(led_interface::msg::LedState),
  LedState_message_member_array,  // message members
  LedState_init_function,  // function to initialize message memory (memory has to be allocated)
  LedState_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t LedState_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &LedState_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace led_interface


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<led_interface::msg::LedState>()
{
  return &::led_interface::msg::rosidl_typesupport_introspection_cpp::LedState_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, led_interface, msg, LedState)() {
  return &::led_interface::msg::rosidl_typesupport_introspection_cpp::LedState_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
