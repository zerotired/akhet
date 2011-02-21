from paste.util.template import paste_script_template_renderer
from pyramid.paster import PyramidTemplate

class AkhetProjectTemplate(PyramidTemplate):
    _template_dir = "akhet"
    summary = "A Pylons-like Pyramid project"
    template_renderer = staticmethod(paste_script_template_renderer)

    def pre(self, command, output_dir, vars): # pragma: no cover
        """Called before template is applied."""
        PyramidTemplate.pre(self, command, output_dir, vars)
        package_logger = vars["package"]
        if package_logger == "root":
            # Rename the app logger in the rare case a project is named 'root'
            package_logger = "app"
        vars["package_logger"] = package_logger