
coelicolor_30s_ribosomal_protein_S7
coelicolor_50s_ribosomal_protein_L7_L12
coelicolor_EFg
coelicolor_EFtu
coelicolor_rpob
coelicolor_rpoc
coelicolor_transcription_antitermination_NUSG

cblaster search -qf query.fasta

cblaster search -qf protein_expression.FASTA -db refseq_protein -eq "txid1902[orgn]" -mh 7 -o summary.cvs -ig -s session.json

# Thsi is a comment


