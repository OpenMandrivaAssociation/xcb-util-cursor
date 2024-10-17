%define major 0
%define libname %mklibname xcb-cursor %{major}
%define devname %mklibname xcb-cursor -d

Summary:	xcb-util's xcb-cursor
Name:		xcb-util-cursor
Version:	0.1.5
Release:	1
Url:		https://xcb.freedesktop.org
Source0:	https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
License:	MIT
Group:		System/X11
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xcb-render)
BuildRequires:	pkgconfig(xcb-renderutil)
BuildRequires:	pkgconfig(xorg-macros)

%description
This is the libXcursor port to XCB.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	xcb-util-cursor library package
Group:		System/X11
Obsoletes:	%{_lib}xcb-util-cursor0 < 0.1.1-2

%description -n %{libname}
This is the libXcursor port to XCB.

%files -n %{libname}
%{_libdir}/libxcb-cursor.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	xcb-util-cursor development files
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{_lib}xcb-util-cursor-devel < 0.1.1-2

%description -n %{devname}
This pakcage includes the development files required to build software against
%{name}.

%files -n %{devname}
%doc ChangeLog NEWS README.md
%{_includedir}/xcb/*.h
%{_libdir}/libxcb-cursor.so
%{_libdir}/pkgconfig/xcb-cursor.pc

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure --disable-static --with-pic
%make_build

%install
%make_install
