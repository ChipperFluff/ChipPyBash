import sys
import os

class Goto:
    """Handles execution jumps by modifying Python's execution flow."""
    
    def __init__(self, file_parser):
        self.labels = file_parser.extract_labels()  # Extract labels from file
        sys.settrace(self.trace_function)  # Enable global tracing

    def trace_function(self, frame, event, arg):
        """Trace function that modifies `f_lineno` safely and prevents skipping."""
        if event in ("call", "line"):
            if "__goto_target" in frame.f_globals:
                frame.f_lineno = frame.f_globals["__goto_target"]
                del frame.f_globals["__goto_target"]  # Remove target after jumping
            return self.trace_function  # Keep tracing active for loops
        return None

    def __call__(self, label):
        """Jumps to a specific label by modifying execution flow."""
        frame = sys._getframe(1)  # Get caller's frame
        if label in self.labels:
            frame.f_globals["__goto_target"] = self.labels[label]  # Store jump target
            sys.settrace(self.trace_function)  # Enable tracing
            sys._getframe().f_trace = sys.gettrace()  # Force execution to re-evaluate immediately
            sys._getframe().f_globals["__force_exec_update"] = True  # Tell Python to update execution
        else:
            raise ValueError(f"Label '{label}' not found")

sys._getframe().f_trace = sys.gettrace()
