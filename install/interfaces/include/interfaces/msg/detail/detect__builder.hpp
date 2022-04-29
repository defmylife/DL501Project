// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/Detect.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__DETECT__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__DETECT__BUILDER_HPP_

#include "interfaces/msg/detail/detect__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_Detect_time_stamp
{
public:
  explicit Init_Detect_time_stamp(::interfaces::msg::Detect & msg)
  : msg_(msg)
  {}
  ::interfaces::msg::Detect time_stamp(::interfaces::msg::Detect::_time_stamp_type arg)
  {
    msg_.time_stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::Detect msg_;
};

class Init_Detect_y2
{
public:
  explicit Init_Detect_y2(::interfaces::msg::Detect & msg)
  : msg_(msg)
  {}
  Init_Detect_time_stamp y2(::interfaces::msg::Detect::_y2_type arg)
  {
    msg_.y2 = std::move(arg);
    return Init_Detect_time_stamp(msg_);
  }

private:
  ::interfaces::msg::Detect msg_;
};

class Init_Detect_x2
{
public:
  explicit Init_Detect_x2(::interfaces::msg::Detect & msg)
  : msg_(msg)
  {}
  Init_Detect_y2 x2(::interfaces::msg::Detect::_x2_type arg)
  {
    msg_.x2 = std::move(arg);
    return Init_Detect_y2(msg_);
  }

private:
  ::interfaces::msg::Detect msg_;
};

class Init_Detect_y1
{
public:
  explicit Init_Detect_y1(::interfaces::msg::Detect & msg)
  : msg_(msg)
  {}
  Init_Detect_x2 y1(::interfaces::msg::Detect::_y1_type arg)
  {
    msg_.y1 = std::move(arg);
    return Init_Detect_x2(msg_);
  }

private:
  ::interfaces::msg::Detect msg_;
};

class Init_Detect_x1
{
public:
  explicit Init_Detect_x1(::interfaces::msg::Detect & msg)
  : msg_(msg)
  {}
  Init_Detect_y1 x1(::interfaces::msg::Detect::_x1_type arg)
  {
    msg_.x1 = std::move(arg);
    return Init_Detect_y1(msg_);
  }

private:
  ::interfaces::msg::Detect msg_;
};

class Init_Detect_confidence
{
public:
  Init_Detect_confidence()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Detect_x1 confidence(::interfaces::msg::Detect::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return Init_Detect_x1(msg_);
  }

private:
  ::interfaces::msg::Detect msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::Detect>()
{
  return interfaces::msg::builder::Init_Detect_confidence();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__DETECT__BUILDER_HPP_
