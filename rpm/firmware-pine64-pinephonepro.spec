Name:       firmware-pine64-pinephonepro
Summary:    Firmware blobs for PinePhone Pro
Version:    1.0
Release:    1
Group:      System/Firmware
License:    Redistributable
URL:        https://github.com/sailfish-on-dontbeevil/firmware-pine64-pinephonepro
Source0:     %{name}-%{version}.tar.bz2
Source1:    dptx.bin
Source2:    brcmfmac43455-sdio.bin
Source3:    BCM4345C0.hcd
Source4:    brcmfmac43455-sdio.txt

%description
This package contains firmware for the Pinephone Pro

%prep
ls -lhR .
%setup -q -n %{name}-%{version}

%build
ls -lR .

%install
pwd
ls -lR .
mkdir -p $RPM_BUILD_ROOT/lib/firmware/brcm
mkdir -p $RPM_BUILD_ROOT/lib/firmware/rockchip
cp %{SOURCE1} $RPM_BUILD_ROOT/lib/firmware/rockchip/
cp %{SOURCE2} $RPM_BUILD_ROOT/lib/firmware/brcm/
cp %{SOURCE3} $RPM_BUILD_ROOT/lib/firmware/brcm/
cp %{SOURCE4} $RPM_BUILD_ROOT/lib/firmware/brcm/

%files
/lib/firmware/
