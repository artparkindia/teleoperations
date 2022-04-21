// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from led_interface:srv/SetLed.idl
// generated code does not contain a copyright notice

#ifndef LED_INTERFACE__SRV__DETAIL__SET_LED__STRUCT_H_
#define LED_INTERFACE__SRV__DETAIL__SET_LED__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in srv/SetLed in the package led_interface.
typedef struct led_interface__srv__SetLed_Request
{
  int16_t led_number;
  bool state;
} led_interface__srv__SetLed_Request;

// Struct for a sequence of led_interface__srv__SetLed_Request.
typedef struct led_interface__srv__SetLed_Request__Sequence
{
  led_interface__srv__SetLed_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} led_interface__srv__SetLed_Request__Sequence;


// Constants defined in the message

// Struct defined in srv/SetLed in the package led_interface.
typedef struct led_interface__srv__SetLed_Response
{
  bool success;
} led_interface__srv__SetLed_Response;

// Struct for a sequence of led_interface__srv__SetLed_Response.
typedef struct led_interface__srv__SetLed_Response__Sequence
{
  led_interface__srv__SetLed_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} led_interface__srv__SetLed_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LED_INTERFACE__SRV__DETAIL__SET_LED__STRUCT_H_
