"""Verify the reusable style's rendering contract, not instruction wording."""
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/sciviz-unit-mpl')
import pathlib, shutil, tempfile, unittest
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
STYLE=pathlib.Path(__file__).resolve().parents[1]/'skills/scientific-visualization/assets/scientific.mplstyle'

class ScientificStyleTests(unittest.TestCase):
    def test_local_style_and_explicit_override(self):
        before=mpl.rcParams['text.usetex']
        with plt.style.context(STYLE):
            self.assertTrue(mpl.rcParams['text.usetex'])
            self.assertGreaterEqual(mpl.rcParams['lines.linewidth'],1.2)
            with mpl.rc_context({'text.usetex':False}):
                self.assertFalse(mpl.rcParams['text.usetex'])
        self.assertEqual(mpl.rcParams['text.usetex'],before)

    def test_export_keeps_fixed_canvas_and_resolution(self):
        with tempfile.TemporaryDirectory() as d, plt.style.context(STYLE), mpl.rc_context({'text.usetex':False}):
            fig,ax=plt.subplots(figsize=(89/25.4,65/25.4),layout='constrained')
            ax.plot([0,1],[0,1]);ax.set(xlabel='Time (s)',ylabel='Velocity (m/s)')
            path=pathlib.Path(d)/'figure.png';fig.savefig(path);plt.close(fig)
            with Image.open(path) as im:
                self.assertAlmostEqual(im.width,89/25.4*300,delta=1)
                self.assertAlmostEqual(im.height,65/25.4*300,delta=1)
                self.assertAlmostEqual(im.info['dpi'][0],300,delta=0.1)

    @unittest.skipUnless(shutil.which('latex') and shutil.which('dvipng'),'LaTeX/PNG tools unavailable')
    def test_real_latex_pdf_and_png_export(self):
        with tempfile.TemporaryDirectory() as d, plt.style.context(STYLE):
            fig,ax=plt.subplots(figsize=(89/25.4,65/25.4),layout='constrained')
            ax.plot([0,1],[0,1],label=r'Model $u$');ax.set(xlabel=r'$t$ (s)',ylabel=r'$u$ (m/s)');ax.legend()
            for suffix in ['pdf','png']:
                p=pathlib.Path(d)/('figure.'+suffix);fig.savefig(p);self.assertGreater(p.stat().st_size,1000)
            plt.close(fig)

if __name__=='__main__': unittest.main()
