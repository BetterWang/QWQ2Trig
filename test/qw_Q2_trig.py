import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process("Q2Trig")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 100

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_dataRun2_v13', '')

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

#fN = cms.untracked.vstring();
#for line in open('flist').read().splitlines():
#	fN.append('file:'+line);
#

flist_t1030 = cms.untracked.vstring();
flist_t3050 = cms.untracked.vstring();
flist_t5070 = cms.untracked.vstring();
flist_b1030 = cms.untracked.vstring();
flist_b3050 = cms.untracked.vstring();
flist_b5070 = cms.untracked.vstring();

for i in range(1, 212):
    flist_t1030.append('file:/afs/cern.ch/user/q/qwang/eos/cms/store/group/phys_heavyions/qwang/PbPb2015/HIFlowCorr/crab_HIFlowCorr_Q2Debug_T1030/160601_132629/0000/Q2_{0}.root'.format(i))
    flist_t3050.append('file:/afs/cern.ch/user/q/qwang/eos/cms/store/group/phys_heavyions/qwang/PbPb2015/HIFlowCorr/crab_HIFlowCorr_Q2Debug_T3050/160601_132648/0000/Q2_{0}.root'.format(i))
    flist_t5070.append('file:/afs/cern.ch/user/q/qwang/eos/cms/store/group/phys_heavyions/qwang/PbPb2015/HIFlowCorr/crab_HIFlowCorr_Q2Debug_T5070/160601_132708/0000/Q2_{0}.root'.format(i))
    flist_b1030.append('file:/afs/cern.ch/user/q/qwang/eos/cms/store/group/phys_heavyions/qwang/PbPb2015/HIFlowCorr/crab_HIFlowCorr_Q2Debug_B1030/160601_132639/0000/Q2_{0}.root'.format(i))
    flist_b3050.append('file:/afs/cern.ch/user/q/qwang/eos/cms/store/group/phys_heavyions/qwang/PbPb2015/HIFlowCorr/crab_HIFlowCorr_Q2Debug_B3050/160601_132658/0000/Q2_{0}.root'.format(i))
    flist_b5070.append('file:/afs/cern.ch/user/q/qwang/eos/cms/store/group/phys_heavyions/qwang/PbPb2015/HIFlowCorr/crab_HIFlowCorr_Q2Debug_B5070/160601_132719/0000/Q2_{0}.root'.format(i))

process.source = cms.Source("PoolSource",
#        fileNames = cms.untracked.vstring("file:/afs/cern.ch/user/q/qwang/eos/cms/store/group/phys_heavyions/qwang/PbPb2015/HIFlowCorr/crab_HIFlowCorr_Q2Debug_T1030/160601_132629/0000/Q2_100.root"),
        fileNames = flist_t1030,
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('q2trig.root')
)


process.Q2Trig = cms.EDAnalyzer('QWQ2Trig'
    , centrality_ = cms.InputTag("centralityBin", "HFtowers")
)

if len(sys.argv)>2:
    if sys.argv[2] == 't1030':
        process.source.fileNames = flist_t1030
        process.TFileService.fileName = cms.string('q2trig_t1030.root')
    if sys.argv[2] == 't3050':
        process.source.fileNames = flist_t3050
        process.TFileService.fileName = cms.string('q2trig_t3050.root')
    if sys.argv[2] == 't5070':
        process.source.fileNames = flist_t5070
        process.TFileService.fileName = cms.string('q2trig_t5070.root')
    if sys.argv[2] == 'b1030':
        process.source.fileNames = flist_b1030
        process.TFileService.fileName = cms.string('q2trig_b1030.root')
    if sys.argv[2] == 'b3050':
        process.source.fileNames = flist_b3050
        process.TFileService.fileName = cms.string('q2trig_b3050.root')
    if sys.argv[2] == 'b5070':
        process.source.fileNames = flist_b5070
        process.TFileService.fileName = cms.string('q2trig_b5070.root')



process.p = cms.Path(process.Q2Trig)
