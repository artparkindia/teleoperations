// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from led_interface:srv/SetLed.idl
// generated code does not contain a copyright notice

#ifndef LED_INTERFACE__SRV__DETAIL__SET_LED__BUILDER_HPP_
#define LED_INTERFACE__SRV__DETAIL__SET_LED__BUILDER_HPP_

#include "led_interface/srv/detail/set_led__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace led_interface
{

namespace srv
{

namespace builder
{

class Init_SetLed_Request_state
{
public:
  explicit Init_SetLed_Request_state(::led_interface::srv::SetLed_Request & msg)
  : msg_(msg)
  {}
  ::led_interface::srv::SetLed_Request state(::led_interface::srv::SetLed_Request::_state_type arg)
  {
    msg_.state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::led_interface::srv::SetLed_Request msg_;
};

class Init_SetLed_Request_led_number
{
public:
  Init_SetLed_Request_led_number()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SetLed_Request_state led_number(::led_interface::srv::SetLed_Request::_led_number_type arg)
  {
    msg_.led_number = std::move(arg);
    return Init_SetLed_Request_state(msg_);
  }

private:
  ::led_interface::srv::SetLed_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::led_interface::srv::SetLed_Request>()
{
  return led_interface::srv::builder::Init_SetLed_Request_led_number();
}

}  // namespace led_interface


namespace led_interface
{

namespace srv
{

namespace builder
{

class Init_SetLed_Response_success
{
public:
  Init_SetLed_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::led_interface::srv::SetLed_Response success(::led_interface::srv::SetLed_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::led_interface::srv::SetLed_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::led_interface::srv::SetLed_Response>()
{
  return led_interface::srv::builder::Init_SetLed_Response_success();
}

}  // namespace led_interface

#endif  // LED_INTERFACE__SRV__DETAIL__SET_LED__BUILDER_HPP_
