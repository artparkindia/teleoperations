// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from led_interface:msg/LedState.idl
// generated code does not contain a copyright notice
#include "led_interface/msg/detail/led_state__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
led_interface__msg__LedState__init(led_interface__msg__LedState * msg)
{
  if (!msg) {
    return false;
  }
  // state
  return true;
}

void
led_interface__msg__LedState__fini(led_interface__msg__LedState * msg)
{
  if (!msg) {
    return;
  }
  // state
}

led_interface__msg__LedState *
led_interface__msg__LedState__create()
{
  led_interface__msg__LedState * msg = (led_interface__msg__LedState *)malloc(sizeof(led_interface__msg__LedState));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(led_interface__msg__LedState));
  bool success = led_interface__msg__LedState__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
led_interface__msg__LedState__destroy(led_interface__msg__LedState * msg)
{
  if (msg) {
    led_interface__msg__LedState__fini(msg);
  }
  free(msg);
}


bool
led_interface__msg__LedState__Sequence__init(led_interface__msg__LedState__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  led_interface__msg__LedState * data = NULL;
  if (size) {
    data = (led_interface__msg__LedState *)calloc(size, sizeof(led_interface__msg__LedState));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = led_interface__msg__LedState__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        led_interface__msg__LedState__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
led_interface__msg__LedState__Sequence__fini(led_interface__msg__LedState__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      led_interface__msg__LedState__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

led_interface__msg__LedState__Sequence *
led_interface__msg__LedState__Sequence__create(size_t size)
{
  led_interface__msg__LedState__Sequence * array = (led_interface__msg__LedState__Sequence *)malloc(sizeof(led_interface__msg__LedState__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = led_interface__msg__LedState__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
led_interface__msg__LedState__Sequence__destroy(led_interface__msg__LedState__Sequence * array)
{
  if (array) {
    led_interface__msg__LedState__Sequence__fini(array);
  }
  free(array);
}
