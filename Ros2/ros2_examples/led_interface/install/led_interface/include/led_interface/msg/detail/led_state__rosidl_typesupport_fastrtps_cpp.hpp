// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from led_interface:msg/LedState.idl
// generated code does not contain a copyright notice

#ifndef LED_INTERFACE__MSG__DETAIL__LED_STATE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define LED_INTERFACE__MSG__DETAIL__LED_STATE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "led_interface/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "led_interface/msg/detail/led_state__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace led_interface
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_led_interface
cdr_serialize(
  const led_interface::msg::LedState & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_led_interface
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  led_interface::msg::LedState & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_led_interface
get_serialized_size(
  const led_interface::msg::LedState & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_led_interface
max_serialized_size_LedState(
  bool & full_bounded,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace led_interface

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_led_interface
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, led_interface, msg, LedState)();

#ifdef __cplusplus
}
#endif

#endif  // LED_INTERFACE__MSG__DETAIL__LED_STATE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
