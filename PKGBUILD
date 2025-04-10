pkgname=storage-kween
pkgver=0.1.0
pkgrel=1
pkgdesc="An elegant GUI storage cleaner for Arch Linux users"
arch=('any')
url="https://github.com/drain/storage-kween"
license=('MIT')
depends=('python' 'python-dearpygui' 'fdupes' 'util-linux' 'pacman-contrib')
makedepends=('git')
optdepends=(
  'zenity: optional GUI dialogs'
  'file: media type detection'
  'imagemagick: image analysis'
  'python-pillow: image processing'
)
source=("$pkgname::git+$url.git")
md5sums=('SKIP')

package() {
  install -Dm755 "$srcdir/$pkgname/storage_kween.py" "$pkgdir/usr/bin/storage-kween"
  install -Dm644 "$srcdir/$pkgname/storage-kween.desktop" "$pkgdir/usr/share/applications/storage-kween.desktop"
  install -Dm644 "$srcdir/$pkgname/icon.svg" "$pkgdir/usr/share/icons/hicolor/scalable/apps/storage-kween.svg"
}
