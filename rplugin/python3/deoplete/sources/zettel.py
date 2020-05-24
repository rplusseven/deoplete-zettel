class Source(Base):
    def __init__(self, vim):
        self.name = 'zettel_files'
        self.mark = '[ZL]'
        self.min_pattern_length = 0
        self.rank = 450
        # only activate for files in my notes directory
        self.filetypes = ['md', 'markdown']

    def get_complete_position(self, context):
        # trigger completion if we're currently in the [[link]] syntax
        pos = context['input'].rfind('[[')
        return pos if pos < 0 else pos + 2

    def gather_candidates(self, context):
        contents = []
        path = '/home/xa/zettel/'
        # now gather all note files, and return paths relative to the current
        # note's directory.
        cur_file_dir = dirname(self.vim.buffers[context['bufnr']].name)
        for fname in glob.iglob(path + '**/*', recursive=True):
            fname = relpath(fname, cur_file_dir)
            if fname.endswith('.md'):
                fname = fname[:-3]
            contents.append(fname)
        return contents
