// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:msg/Detect.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__DETECT__STRUCT_HPP_
#define INTERFACES__MSG__DETAIL__DETECT__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__interfaces__msg__Detect __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__msg__Detect __declspec(deprecated)
#endif

namespace interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Detect_
{
  using Type = Detect_<ContainerAllocator>;

  explicit Detect_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->confidence = 0.0;
      this->x1 = 0.0;
      this->y1 = 0.0;
      this->x2 = 0.0;
      this->y2 = 0.0;
      this->time_stamp = 0ll;
    }
  }

  explicit Detect_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->confidence = 0.0;
      this->x1 = 0.0;
      this->y1 = 0.0;
      this->x2 = 0.0;
      this->y2 = 0.0;
      this->time_stamp = 0ll;
    }
  }

  // field types and members
  using _confidence_type =
    double;
  _confidence_type confidence;
  using _x1_type =
    double;
  _x1_type x1;
  using _y1_type =
    double;
  _y1_type y1;
  using _x2_type =
    double;
  _x2_type x2;
  using _y2_type =
    double;
  _y2_type y2;
  using _time_stamp_type =
    int64_t;
  _time_stamp_type time_stamp;

  // setters for named parameter idiom
  Type & set__confidence(
    const double & _arg)
  {
    this->confidence = _arg;
    return *this;
  }
  Type & set__x1(
    const double & _arg)
  {
    this->x1 = _arg;
    return *this;
  }
  Type & set__y1(
    const double & _arg)
  {
    this->y1 = _arg;
    return *this;
  }
  Type & set__x2(
    const double & _arg)
  {
    this->x2 = _arg;
    return *this;
  }
  Type & set__y2(
    const double & _arg)
  {
    this->y2 = _arg;
    return *this;
  }
  Type & set__time_stamp(
    const int64_t & _arg)
  {
    this->time_stamp = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::msg::Detect_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::msg::Detect_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::msg::Detect_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::msg::Detect_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::Detect_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::Detect_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::Detect_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::Detect_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::msg::Detect_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::msg::Detect_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__msg__Detect
    std::shared_ptr<interfaces::msg::Detect_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__msg__Detect
    std::shared_ptr<interfaces::msg::Detect_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Detect_ & other) const
  {
    if (this->confidence != other.confidence) {
      return false;
    }
    if (this->x1 != other.x1) {
      return false;
    }
    if (this->y1 != other.y1) {
      return false;
    }
    if (this->x2 != other.x2) {
      return false;
    }
    if (this->y2 != other.y2) {
      return false;
    }
    if (this->time_stamp != other.time_stamp) {
      return false;
    }
    return true;
  }
  bool operator!=(const Detect_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Detect_

// alias to use template instance with default allocator
using Detect =
  interfaces::msg::Detect_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__DETECT__STRUCT_HPP_
