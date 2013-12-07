%define major 0
%define libname %mklibname %{name} %major
%define develname %mklibname %{name} -d

Summary:	xcb-util's xcb-cursor
Name:		xcb-util-cursor
Version:	0.1.0
Release:	3
Url:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
License:	MIT
Group:		System/X11
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xcb-render)
BuildRequires:	pkgconfig(xcb-renderutil)
BuildRequires:	pkgconfig(xorg-macros)

%description
This is the libXcursor port to XCB.

%package -n %{libname}
Summary: xcb-util-cursor library package
Group: System/X11

%description -n %{libname}
This is the libXcursor port to XCB.

%package -n %{develname}
Summary: xcb-util-cursor development files
Group: Development/C
Provides:  libxcb-util-cursor-devel = %{version}-%{release}
Provides:  xcb-util-cursor-devel = %{version}-%{release}
Requires:  %{libname} = %{version}-%{release}

%description -n %{develname}
This pakcage includes the development files required to build software against
%{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%{_libdir}/libxcb-cursor.so.%{major}*

%files -n %{develname}
%doc ChangeLog NEWS README
%{_includedir}/xcb/*.h
%{_libdir}/libxcb-cursor.so
%{_libdir}/pkgconfig/xcb-cursor.pc
