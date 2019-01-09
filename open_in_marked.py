import subprocess
import sys

import sublime
import sublime_plugin

class OpenInMarkedAppCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    if sys.platform.startswith('darwin'):
      self.view.run_command('save')
      subprocess.call(['open', '-b', 'com.brettterpstra.marked2', self.view.file_name()])
