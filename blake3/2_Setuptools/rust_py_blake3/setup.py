import sys
from setuptools import setup

try:
    from setuptools_rust import Binding, RustExtension
except ImportError:
    import subprocess
    errno = subprocess.call(
        [sys.executable, '-m', 'pip', 'install', 'setuptools-rust'])
    if errno:
        print("Please install setuptools-rust package")
        raise SystemExit(errno)
    else:
        from setuptools_rust import Binding, RustExtension

setup_requires = ['setuptools-rust>=0.9.2']
install_requires = []

setup(name='rust_py_blake3',
      version='0.1.0',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Rust',
          'Operating System :: POSIX',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows'
      ],
      rust_extensions=[
          RustExtension('rust_py_blake3.rust_py_blake3', 'Cargo.toml', binding=Binding.PyO3)],
      packages=['rust_py_blake3'],
      zip_safe=False)