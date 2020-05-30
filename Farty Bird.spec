# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Farty Bird.py'],
             pathex=['/Users/lampwick17/Documents/VSCode_FartyBird'],
             binaries=[],
             datas=[('assets','assets'),('main.py','.')],
             hiddenimports=['pygame', 'time', 'random', 'os', 'math', 'csv', 'pygame.locals','pkg_resources.py2_warn','sys'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['numpy'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Farty Bird',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Farty Bird')
app = BUNDLE(coll,
             name='Farty Bird.app',
             icon=None,
             bundle_identifier=None)
