#for getting locals, globals and path for corresponding module.
import inspect

class PygameLive():
    def __find_function(self, file_path, function_name):
        """
       Finds the method for live coding.
        """

        #opens the method file.
        with open(file_path, 'r') as f:
            file_contents = f.readlines()

        #method declaration part
        declaration = ""
        # method body part
        body = ""
        #flag for method found or not.
        found = False
        #indentation check if the new line indentation is less than method it triggers keyword break
        l = None
        comment = False
        #checking each line
        for line in file_contents:
            #filtering white spaces and comments
            if not any([line.lstrip().startswith("\n") ,line.lstrip().startswith("#")]):
                if found:
                    num_whitespace_chars = len(line) - len(line.lstrip())
                    if not l : l = num_whitespace_chars

                    if l and ( num_whitespace_chars < l):
                        break
                    #filtering multiline comments.
                    if line.strip().startswith("'''") or line.strip().startswith('"""'):
                        comment = True
                
                    if line.strip().endswith("'''") or line.strip().endswith('"""'):
                        comment = False
                        continue
            
                    if comment:
                        continue
                    
                    body += line
                    
                elif line.strip().startswith("def " + function_name):
                    declaration += "\n" + line.lstrip()
                    found = True
        #filtered code string to execute.
        return declaration + body

    def debug(self,method):
        """
              Args:
                  method (Object): Insert draw or update method of your game class.Name should be unique

              Returns:
                  str: The contents of the function as a string.
        """
        #points to the caller module namespace.
        calling_frame = inspect.currentframe().f_back

        #locals and global namespaces of corresponding module.
        local_namespace = calling_frame.f_locals
        global_namespace = calling_frame.f_globals

        # caller modoule path
        file_path = global_namespace["__file__"]

        #gets code string to exec
        codes = self.__find_function(file_path, method.__name__)
        #executing function
        exec(codes + f"\n{method.__name__}(self)\n", global_namespace, local_namespace)
        #returns code string if needed.
        return codes