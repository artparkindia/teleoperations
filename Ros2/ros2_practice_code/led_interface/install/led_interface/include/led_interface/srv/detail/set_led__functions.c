// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from led_interface:srv/SetLed.idl
// generated code does not contain a copyright notice
#include "led_interface/srv/detail/set_led__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool
led_interface__srv__SetLed_Request__init(led_interface__srv__SetLed_Request * msg)
{
  if (!msg) {
    return false;
  }
  // led_number
  // state
  return true;
}

void
led_interface__srv__SetLed_Request__fini(led_interface__srv__SetLed_Request * msg)
{
  if (!msg) {
    return;
  }
  // led_number
  // state
}

led_interface__srv__SetLed_Request *
led_interface__srv__SetLed_Request__create()
{
  led_interface__srv__SetLed_Request * msg = (led_interface__srv__SetLed_Request *)malloc(sizeof(led_interface__srv__SetLed_Request));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(led_interface__srv__SetLed_Request));
  bool success = led_interface__srv__SetLed_Request__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
led_interface__srv__SetLed_Request__destroy(led_interface__srv__SetLed_Request * msg)
{
  if (msg) {
    led_interface__srv__SetLed_Request__fini(msg);
  }
  free(msg);
}


bool
led_interface__srv__SetLed_Request__Sequence__init(led_interface__srv__SetLed_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  led_interface__srv__SetLed_Request * data = NULL;
  if (size) {
    data = (led_interface__srv__SetLed_Request *)calloc(size, sizeof(led_interface__srv__SetLed_Request));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = led_interface__srv__SetLed_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        led_interface__srv__SetLed_Request__fini(&data[i - 1]);
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
led_interface__srv__SetLed_Request__Sequence__fini(led_interface__srv__SetLed_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      led_interface__srv__SetLed_Request__fini(&array->data[i]);
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

led_interface__srv__SetLed_Request__Sequence *
led_interface__srv__SetLed_Request__Sequence__create(size_t size)
{
  led_interface__srv__SetLed_Request__Sequence * array = (led_interface__srv__SetLed_Request__Sequence *)malloc(sizeof(led_interface__srv__SetLed_Request__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = led_interface__srv__SetLed_Request__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
led_interface__srv__SetLed_Request__Sequence__destroy(led_interface__srv__SetLed_Request__Sequence * array)
{
  if (array) {
    led_interface__srv__SetLed_Request__Sequence__fini(array);
  }
  free(array);
}


bool
led_interface__srv__SetLed_Response__init(led_interface__srv__SetLed_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  return true;
}

void
led_interface__srv__SetLed_Response__fini(led_interface__srv__SetLed_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
}

led_interface__srv__SetLed_Response *
led_interface__srv__SetLed_Response__create()
{
  led_interface__srv__SetLed_Response * msg = (led_interface__srv__SetLed_Response *)malloc(sizeof(led_interface__srv__SetLed_Response));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(led_interface__srv__SetLed_Response));
  bool success = led_interface__srv__SetLed_Response__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
led_interface__srv__SetLed_Response__destroy(led_interface__srv__SetLed_Response * msg)
{
  if (msg) {
    led_interface__srv__SetLed_Response__fini(msg);
  }
  free(msg);
}


bool
led_interface__srv__SetLed_Response__Sequence__init(led_interface__srv__SetLed_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  led_interface__srv__SetLed_Response * data = NULL;
  if (size) {
    data = (led_interface__srv__SetLed_Response *)calloc(size, sizeof(led_interface__srv__SetLed_Response));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = led_interface__srv__SetLed_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        led_interface__srv__SetLed_Response__fini(&data[i - 1]);
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
led_interface__srv__SetLed_Response__Sequence__fini(led_interface__srv__SetLed_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      led_interface__srv__SetLed_Response__fini(&array->data[i]);
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

led_interface__srv__SetLed_Response__Sequence *
led_interface__srv__SetLed_Response__Sequence__create(size_t size)
{
  led_interface__srv__SetLed_Response__Sequence * array = (led_interface__srv__SetLed_Response__Sequence *)malloc(sizeof(led_interface__srv__SetLed_Response__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = led_interface__srv__SetLed_Response__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
led_interface__srv__SetLed_Response__Sequence__destroy(led_interface__srv__SetLed_Response__Sequence * array)
{
  if (array) {
    led_interface__srv__SetLed_Response__Sequence__fini(array);
  }
  free(array);
}
