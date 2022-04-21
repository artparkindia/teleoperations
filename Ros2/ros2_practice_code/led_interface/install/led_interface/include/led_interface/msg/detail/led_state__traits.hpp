// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from led_interface:msg/LedState.idl
// generated code does not contain a copyright notice

#ifndef LED_INTERFACE__MSG__DETAIL__LED_STATE__TRAITS_HPP_
#define LED_INTERFACE__MSG__DETAIL__LED_STATE__TRAITS_HPP_

#include "led_interface/msg/detail/led_state__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const led_interface::msg::LedState & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.state.size() == 0) {
      out << "state: []\n";
    } else {
      out << "state:\n";
      for (auto item : msg.state) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const led_interface::msg::LedState & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<led_interface::msg::LedState>()
{
  return "led_interface::msg::LedState";
}

template<>
inline const char * name<led_interface::msg::LedState>()
{
  return "led_interface/msg/LedState";
}

template<>
struct has_fixed_size<led_interface::msg::LedState>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<led_interface::msg::LedState>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<led_interface::msg::LedState>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // LED_INTERFACE__MSG__DETAIL__LED_STATE__TRAITS_HPP_
