// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from led_interface:srv/SetLed.idl
// generated code does not contain a copyright notice

#ifndef LED_INTERFACE__SRV__DETAIL__SET_LED__TRAITS_HPP_
#define LED_INTERFACE__SRV__DETAIL__SET_LED__TRAITS_HPP_

#include "led_interface/srv/detail/set_led__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const led_interface::srv::SetLed_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: led_number
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "led_number: ";
    value_to_yaml(msg.led_number, out);
    out << "\n";
  }

  // member: state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "state: ";
    value_to_yaml(msg.state, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const led_interface::srv::SetLed_Request & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<led_interface::srv::SetLed_Request>()
{
  return "led_interface::srv::SetLed_Request";
}

template<>
inline const char * name<led_interface::srv::SetLed_Request>()
{
  return "led_interface/srv/SetLed_Request";
}

template<>
struct has_fixed_size<led_interface::srv::SetLed_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<led_interface::srv::SetLed_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<led_interface::srv::SetLed_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

inline void to_yaml(
  const led_interface::srv::SetLed_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const led_interface::srv::SetLed_Response & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<led_interface::srv::SetLed_Response>()
{
  return "led_interface::srv::SetLed_Response";
}

template<>
inline const char * name<led_interface::srv::SetLed_Response>()
{
  return "led_interface/srv/SetLed_Response";
}

template<>
struct has_fixed_size<led_interface::srv::SetLed_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<led_interface::srv::SetLed_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<led_interface::srv::SetLed_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<led_interface::srv::SetLed>()
{
  return "led_interface::srv::SetLed";
}

template<>
inline const char * name<led_interface::srv::SetLed>()
{
  return "led_interface/srv/SetLed";
}

template<>
struct has_fixed_size<led_interface::srv::SetLed>
  : std::integral_constant<
    bool,
    has_fixed_size<led_interface::srv::SetLed_Request>::value &&
    has_fixed_size<led_interface::srv::SetLed_Response>::value
  >
{
};

template<>
struct has_bounded_size<led_interface::srv::SetLed>
  : std::integral_constant<
    bool,
    has_bounded_size<led_interface::srv::SetLed_Request>::value &&
    has_bounded_size<led_interface::srv::SetLed_Response>::value
  >
{
};

template<>
struct is_service<led_interface::srv::SetLed>
  : std::true_type
{
};

template<>
struct is_service_request<led_interface::srv::SetLed_Request>
  : std::true_type
{
};

template<>
struct is_service_response<led_interface::srv::SetLed_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // LED_INTERFACE__SRV__DETAIL__SET_LED__TRAITS_HPP_
