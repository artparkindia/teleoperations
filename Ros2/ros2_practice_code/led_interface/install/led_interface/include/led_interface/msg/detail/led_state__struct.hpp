// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from led_interface:msg/LedState.idl
// generated code does not contain a copyright notice

#ifndef LED_INTERFACE__MSG__DETAIL__LED_STATE__STRUCT_HPP_
#define LED_INTERFACE__MSG__DETAIL__LED_STATE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__led_interface__msg__LedState __attribute__((deprecated))
#else
# define DEPRECATED__led_interface__msg__LedState __declspec(deprecated)
#endif

namespace led_interface
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct LedState_
{
  using Type = LedState_<ContainerAllocator>;

  explicit LedState_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<int16_t, 3>::iterator, int16_t>(this->state.begin(), this->state.end(), 0);
    }
  }

  explicit LedState_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : state(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<int16_t, 3>::iterator, int16_t>(this->state.begin(), this->state.end(), 0);
    }
  }

  // field types and members
  using _state_type =
    std::array<int16_t, 3>;
  _state_type state;

  // setters for named parameter idiom
  Type & set__state(
    const std::array<int16_t, 3> & _arg)
  {
    this->state = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    led_interface::msg::LedState_<ContainerAllocator> *;
  using ConstRawPtr =
    const led_interface::msg::LedState_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<led_interface::msg::LedState_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<led_interface::msg::LedState_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      led_interface::msg::LedState_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<led_interface::msg::LedState_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      led_interface::msg::LedState_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<led_interface::msg::LedState_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<led_interface::msg::LedState_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<led_interface::msg::LedState_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__led_interface__msg__LedState
    std::shared_ptr<led_interface::msg::LedState_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__led_interface__msg__LedState
    std::shared_ptr<led_interface::msg::LedState_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const LedState_ & other) const
  {
    if (this->state != other.state) {
      return false;
    }
    return true;
  }
  bool operator!=(const LedState_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct LedState_

// alias to use template instance with default allocator
using LedState =
  led_interface::msg::LedState_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace led_interface

#endif  // LED_INTERFACE__MSG__DETAIL__LED_STATE__STRUCT_HPP_
