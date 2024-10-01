#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v20
# autospec commit: f35655a
#
Name     : R-glue
Version  : 1.8.0
Release  : 68
URL      : https://cran.r-project.org/src/contrib/glue_1.8.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/glue_1.8.0.tar.gz
Summary  : Interpreted String Literals
Group    : Development/Tools
License  : MIT
Requires: R-glue-lib = %{version}-%{release}
BuildRequires : R-evaluate
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Python's Literal String Interpolation

%package lib
Summary: lib components for the R-glue package.
Group: Libraries

%description lib
lib components for the R-glue package.


%prep
%setup -q -n glue
pushd ..
cp -a glue buildavx2
popd
pushd ..
cp -a glue buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1727794092

%install
export SOURCE_DATE_EPOCH=1727794092
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/glue/DESCRIPTION
/usr/lib64/R/library/glue/INDEX
/usr/lib64/R/library/glue/LICENSE
/usr/lib64/R/library/glue/Meta/Rd.rds
/usr/lib64/R/library/glue/Meta/features.rds
/usr/lib64/R/library/glue/Meta/hsearch.rds
/usr/lib64/R/library/glue/Meta/links.rds
/usr/lib64/R/library/glue/Meta/nsInfo.rds
/usr/lib64/R/library/glue/Meta/package.rds
/usr/lib64/R/library/glue/Meta/vignette.rds
/usr/lib64/R/library/glue/NAMESPACE
/usr/lib64/R/library/glue/NEWS.md
/usr/lib64/R/library/glue/R/glue
/usr/lib64/R/library/glue/R/glue.rdb
/usr/lib64/R/library/glue/R/glue.rdx
/usr/lib64/R/library/glue/doc/engines.R
/usr/lib64/R/library/glue/doc/engines.Rmd
/usr/lib64/R/library/glue/doc/engines.html
/usr/lib64/R/library/glue/doc/glue.R
/usr/lib64/R/library/glue/doc/glue.Rmd
/usr/lib64/R/library/glue/doc/glue.html
/usr/lib64/R/library/glue/doc/index.html
/usr/lib64/R/library/glue/doc/transformers.R
/usr/lib64/R/library/glue/doc/transformers.Rmd
/usr/lib64/R/library/glue/doc/transformers.html
/usr/lib64/R/library/glue/doc/wrappers.R
/usr/lib64/R/library/glue/doc/wrappers.Rmd
/usr/lib64/R/library/glue/doc/wrappers.html
/usr/lib64/R/library/glue/help/AnIndex
/usr/lib64/R/library/glue/help/aliases.rds
/usr/lib64/R/library/glue/help/figures/logo.png
/usr/lib64/R/library/glue/help/glue.rdb
/usr/lib64/R/library/glue/help/glue.rdx
/usr/lib64/R/library/glue/help/paths.rds
/usr/lib64/R/library/glue/html/00Index.html
/usr/lib64/R/library/glue/html/R.css
/usr/lib64/R/library/glue/tests/testthat.R
/usr/lib64/R/library/glue/tests/testthat/_snaps/color.md
/usr/lib64/R/library/glue/tests/testthat/_snaps/glue.md
/usr/lib64/R/library/glue/tests/testthat/_snaps/sql.md
/usr/lib64/R/library/glue/tests/testthat/_snaps/transformer.md
/usr/lib64/R/library/glue/tests/testthat/test-collapse.R
/usr/lib64/R/library/glue/tests/testthat/test-color.R
/usr/lib64/R/library/glue/tests/testthat/test-glue.R
/usr/lib64/R/library/glue/tests/testthat/test-quoting.R
/usr/lib64/R/library/glue/tests/testthat/test-safe.R
/usr/lib64/R/library/glue/tests/testthat/test-sql.R
/usr/lib64/R/library/glue/tests/testthat/test-transformer.R
/usr/lib64/R/library/glue/tests/testthat/test-trim.R
/usr/lib64/R/library/glue/tests/testthat/test-vctrs.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/glue/libs/glue.so
/V4/usr/lib64/R/library/glue/libs/glue.so
/usr/lib64/R/library/glue/libs/glue.so
