import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "holden_et_al2005"

    def cmd_makecldf(self, args):
        self.init(args)
        
        # Add summary tree (e.g. MCCT or Consensus)
        summary = self.raw_dir.read_tree('BantuBinRed_m1pcv.mcct.trees', detranslate=True)
        args.writer.add_summary(summary, self.metadata, args.log)

        # Add posterior tree distribution
        # 1000 trees, 20% burnin
        posterior = self.raw_dir.read_trees(
            'BantuBinRed_m1pcv.nex.trees.gz', burnin=21, detranslate=True)
        args.writer.add_posterior(posterior, self.metadata, args.log)
        
        # Add nexus data
        data = self.raw_dir.read_nexus('BantuBinRed_m1pcv.nex')
        args.writer.add_data(data, self.characters, args.log)
