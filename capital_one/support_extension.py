
# FORMAT:
# {     extension1: [ single_cmt, multi_cmt_start, multi_cmt_end],
#       extension2: [ single_cmt, multi_cmt_start, multi_cmt_end],
#       extension3: [ single_cmt, multi_cmt_start, multi_cmt_end] }

SUPPORT_EXTENSION = {'.py': ["#", None, None],          # Python
                     '.sh': ["#", None, None],          # shell
                     '.bash': ["#", None, None],        # bash
                     '.java': ["//", "/*", "*/"],       # Java
                     '.js': ["//", "/*", "*/"],         # JavaScript
                     '.c': ["//", "/*", "*/"],          # C
                     '.cpp': ["//", "/*", "*/"],        # C++
                     '.swift': ["//", "/*", "*/"],      # Swift
                     '.sql': ["--", "/*", "*/"],        # SQL
                     '.rb': ["-", "=begin", "=end"]     # Ruby
                     }

