class Payloads:
    def ls(self):
        proc = subprocess.check_output(['ls', 'PayLoads'])
        proc = proc.decode()
        lst = proc.split()
        try:
            lst.remove('__main__.py')
            lst.remove('__pycache__')
        except:
            pass
        for i in lst:
            print(i)
    
    def cp(self, p, pn):
        subprocess.check_output(['cp', f'./PayLoads/{p}', f'./{pn}'])
        print('Done.')

    def main(self):
        self.ls()
        pl = input('payload:')
        pln = input(f'payload name ({pl}):')
        self.cp(pl, pln)


if __name__ == '__main__':
    import subprocess

    p = Payloads()
    p.main()
