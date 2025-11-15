import sys
import io

class CodeExecTool:
    """
    CodeExecTool: Executes Python code snippets safely
    """
    def execute(self, code: str):
        """
        Executes Python code and returns stdout and stderr
        """
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        redirected_output = sys.stdout = io.StringIO()
        redirected_error = sys.stderr = io.StringIO()
        try:
            exec(code, {})
        except Exception as e:
            error = str(e)
        else:
            error = None
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        output = redirected_output.getvalue()
        return {"output": output.strip(), "error": error or redirected_error.getvalue().strip()}
