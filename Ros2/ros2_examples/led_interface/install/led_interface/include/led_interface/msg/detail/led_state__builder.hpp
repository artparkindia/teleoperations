// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from led_interface:msg/LedState.idl
// generated code does not contain a copyright notice

#ifndef LED_INTERFACE__MSG__DETAIL__LED_STATE__BUILDER_HPP_
#define LED_INTERFACE__MSG__DETAIL__LED_STATE__BUILDER_HPP_

#include "led_interface/msg/detail/led_state__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace led_interface
{

namespace msg
{

namespace builder
{

class Init_LedState_state
{
public:
  Init_LedState_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::led_interface::msg::LedState state(::led_interface::msg::LedState::_state_type arg)
  {
    msg_.state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::led_interface::msg::LedState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::led_interface::msg::LedState>()
{
  return led_interface::msg::builder::Init_LedState_state();
}

}  // namespace led_interface

#endif  // LED_INTERFACE__MSG__DETAIL__LED_STATE__BUILDER_HPP_
