// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:msg/Detect.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__DETECT__TRAITS_HPP_
#define INTERFACES__MSG__DETAIL__DETECT__TRAITS_HPP_

#include "interfaces/msg/detail/detect__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::msg::Detect>()
{
  return "interfaces::msg::Detect";
}

template<>
inline const char * name<interfaces::msg::Detect>()
{
  return "interfaces/msg/Detect";
}

template<>
struct has_fixed_size<interfaces::msg::Detect>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::msg::Detect>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::msg::Detect>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__MSG__DETAIL__DETECT__TRAITS_HPP_
