%global kf5_version 5.116.0

Name:           opt-kf5-threadweaver
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon for advanced thread management
License:        LGPLv2+
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  opt-extra-cmake-modules >= %{kf5_version}
BuildRequires:  opt-kf5-rpm-macros
BuildRequires:  opt-qt5-qtbase-devel

%{?opt_kf5_default_filter}

%description
KDE Frameworks 5 Tier 1 addon for advanced thread management.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       opt-qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../ \
  -DKDE_INSTALL_LIBEXECDIR=%{_opt_kf5_libexecdir}
%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc README.md
%license LICENSES/*.txt
%{_opt_kf5_libdir}/libKF5ThreadWeaver.so.*

%files devel
%{_opt_kf5_includedir}/KF5/ThreadWeaver/
%{_opt_kf5_libdir}/libKF5ThreadWeaver.so
%{_opt_kf5_libdir}/cmake/KF5ThreadWeaver/
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_ThreadWeaver.pri
