// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from led_interface:msg/LedState.idl
// generated code does not contain a copyright notice

#ifndef LED_INTERFACE__MSG__DETAIL__LED_STATE__STRUCT_H_
#define LED_INTERFACE__MSG__DETAIL__LED_STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/LedState in the package led_interface.
typedef struct led_interface__msg__LedState
{
  int16_t state[3];
} led_interface__msg__LedState;

// Struct for a sequence of led_interface__msg__LedState.
typedef struct led_interface__msg__LedState__Sequence
{
  led_interface__msg__LedState * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} led_interface__msg__LedState__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LED_INTERFACE__MSG__DETAIL__LED_STATE__STRUCT_H_
