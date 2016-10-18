Name:           ros-minimalist-catkin
Version:        0.7.4
Release:        3%{?dist}
Summary:        ROS catkin package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/catkin
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       cmake
Requires:       gtest-devel
Requires:       python
Requires:       python-catkin_pkg > 0.2.9
Requires:       python-empy
Requires:       python-nose
BuildRequires:  cmake
BuildRequires:  python
BuildRequires:  python-catkin_pkg > 0.2.9
BuildRequires:  python-empy
BuildRequires:  python-mock
BuildRequires:  python-nose

%description
Low-level build system macros and infrastructure for ROS.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/minimalist/setup.sh" ]; then . "/opt/ros/minimalist/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/minimalist" \
        -DCMAKE_PREFIX_PATH="/opt/ros/minimalist" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/minimalist/setup.sh" ]; then . "/opt/ros/minimalist/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/minimalist

%changelog
* Tue Oct 18 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.7.4-3
- Autogenerated by Bloom

* Tue Oct 18 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.7.4-2
- Autogenerated by Bloom

* Tue Oct 18 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.7.4-1
- Autogenerated by Bloom

* Tue Oct 18 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.7.4-0
- Autogenerated by Bloom

