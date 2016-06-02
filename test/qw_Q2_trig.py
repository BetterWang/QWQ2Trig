import FWCore.ParameterSet.Config as cms

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
    flist_t1030.append('file:/afs/cern.ch/user/q/qwang/eos/cms/store/group/phys_heavyions/qwang/PbPb2015/HIFlowCorr/crab_HIFlowCorr_Q2Debug_T1030/160601_132629/0000/Q2_{i}.root'.format(i))
    flist_t3050.append('file:/afs/cern.ch/user/q/qwang/eos/cms/store/group/phys_heavyions/qwang/PbPb2015/HIFlowCorr/crab_HIFlowCorr_Q2Debug_T3050/160601_132648/0000/Q2_{i}.root'.format(i))
    flist_t5070.append('file:/afs/cern.ch/user/q/qwang/eos/cms/store/group/phys_heavyions/qwang/PbPb2015/HIFlowCorr/crab_HIFlowCorr_Q2Debug_T5070/160601_132708/0000/Q2_{i}.root'.format(i))
    flist_b1030.append('file:/afs/cern.ch/user/q/qwang/eos/cms/store/group/phys_heavyions/qwang/PbPb2015/HIFlowCorr/crab_HIFlowCorr_Q2Debug_B1030/160601_132639/0000/Q2_{i}.root'.format(i))
    flist_b3050.append('file:/afs/cern.ch/user/q/qwang/eos/cms/store/group/phys_heavyions/qwang/PbPb2015/HIFlowCorr/crab_HIFlowCorr_Q2Debug_B3050/160601_132658/0000/Q2_{i}.root'.format(i))
    flist_b5070.append('file:/afs/cern.ch/user/q/qwang/eos/cms/store/group/phys_heavyions/qwang/PbPb2015/HIFlowCorr/crab_HIFlowCorr_Q2Debug_B5070/160601_132719/0000/Q2_{i}.root'.format(i))

process.source = cms.Source("PoolSource",
#        fileNames = cms.untracked.vstring("file:/afs/cern.ch/user/q/qwang/eos/cms/store/group/phys_heavyions/qwang/PbPb2015/HIFlowCorr/crab_HIFlowCorr_Q2Debug_T1030/160601_132629/0000/Q2_100.root"),
        fileNames = flist_t1030,
)


process.Q2Trig = cms.EDAnalyzer('QWQ2Trig'
    , centrality_ = cms.InputTag("centralityBin", "HFtowers")
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('q2trig.root')
)

process.p = cms.Path(process.Q2Trig)
