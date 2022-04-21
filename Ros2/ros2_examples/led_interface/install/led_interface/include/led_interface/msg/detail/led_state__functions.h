// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from led_interface:msg/LedState.idl
// generated code does not contain a copyright notice

#ifndef LED_INTERFACE__MSG__DETAIL__LED_STATE__FUNCTIONS_H_
#define LED_INTERFACE__MSG__DETAIL__LED_STATE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "led_interface/msg/rosidl_generator_c__visibility_control.h"

#include "led_interface/msg/detail/led_state__struct.h"

/// Initialize msg/LedState message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * led_interface__msg__LedState
 * )) before or use
 * led_interface__msg__LedState__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_led_interface
bool
led_interface__msg__LedState__init(led_interface__msg__LedState * msg);

/// Finalize msg/LedState message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_led_interface
void
led_interface__msg__LedState__fini(led_interface__msg__LedState * msg);

/// Create msg/LedState message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * led_interface__msg__LedState__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_led_interface
led_interface__msg__LedState *
led_interface__msg__LedState__create();

/// Destroy msg/LedState message.
/**
 * It calls
 * led_interface__msg__LedState__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_led_interface
void
led_interface__msg__LedState__destroy(led_interface__msg__LedState * msg);


/// Initialize array of msg/LedState messages.
/**
 * It allocates the memory for the number of elements and calls
 * led_interface__msg__LedState__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_led_interface
bool
led_interface__msg__LedState__Sequence__init(led_interface__msg__LedState__Sequence * array, size_t size);

/// Finalize array of msg/LedState messages.
/**
 * It calls
 * led_interface__msg__LedState__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_led_interface
void
led_interface__msg__LedState__Sequence__fini(led_interface__msg__LedState__Sequence * array);

/// Create array of msg/LedState messages.
/**
 * It allocates the memory for the array and calls
 * led_interface__msg__LedState__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_led_interface
led_interface__msg__LedState__Sequence *
led_interface__msg__LedState__Sequence__create(size_t size);

/// Destroy array of msg/LedState messages.
/**
 * It calls
 * led_interface__msg__LedState__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_led_interface
void
led_interface__msg__LedState__Sequence__destroy(led_interface__msg__LedState__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // LED_INTERFACE__MSG__DETAIL__LED_STATE__FUNCTIONS_H_
