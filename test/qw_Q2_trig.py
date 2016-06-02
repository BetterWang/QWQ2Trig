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

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring("file:FullTrack_1.root")
)


process.Q2Trig = cms.EDAnalyzer('QWQ2Trig'
    , centrality_ = cms.InputTag("centralityBin", "HFtowers")
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('q2trig.root')
)

process.p = cms.Path(process.Q2Trig)
