Name:       alsa-scenario-scn-data-0-emul
Summary:    alsa scenario data for emulator codec
Version:    0.1.1
Release:    2
Group:      TO_BE/FILLED_IN
License:    LGPLv2.1
ExclusiveArch: %{ix86} 
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/alsa-scenario-scn-data-0-emul.manifest

%description
Alsa scenario data for emulator codec

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/etc/sound
cp -a emul %{buildroot}/usr/etc/sound
cp -a emul.conf %{buildroot}/usr/etc/sound/emul.conf

%post
BASE_PATH=/usr/etc/sound
CODEC=emul

chmod 644 $BASE_PATH/$CODEC/*
chmod 644 $BASE_PATH/$CODEC.conf

chown -R 0:6822 $BASE_PATH/$CODEC
chown 0:6822 $BASE_PATH/$CODEC.conf

ln -s $BASE_PATH/$CODEC $BASE_PATH/default
ln -s $BASE_PATH/$CODEC.conf $BASE_PATH/default.conf

%preun
BASE_PATH=/usr/etc/sound

rm -f $BASE_PATH/default.conf
rm -f $BASE_PATH/default


%files
/usr/etc/sound/*
