#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/HeavyIonEvent/interface/EvtPlane.h"
#include <RecoHI/HiEvtPlaneAlgos/interface/HiEvtPlaneList.h>
#include "TH1.h"
#include "TH2.h"
#include "TNtuple.h"
#include "TComplex.h"
#include <complex>


class QWQ2Trig : public edm::EDAnalyzer {
	public:
		explicit QWQ2Trig(const edm::ParameterSet&);
		~QWQ2Trig();

		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

	private:
		virtual void beginJob() override;
		virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
		virtual void endJob() override;

//		virtual void beginRun(edm::Run const&, edm::EventSetup const&);
//		virtual void endRun(edm::Run const&, edm::EventSetup const&);
//		virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
//		virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

		edm::EDGetTokenT<reco::EvtPlaneCollection>	epToken_;
		edm::EDGetTokenT<int>				centralityToken_;
		TH1D *hCent_v1, *hCent_v2, *hCent_v3;
		TH1D *hQ2_v1, *hQ2_v2, *hQ2_v3;
};

QWQ2Trig::QWQ2Trig(const edm::ParameterSet& iConfig) :
	epToken_( consumes<reco::EvtPlaneCollection>(iConfig.getUntrackedParameter<edm::InputTag>("epSrc", std::string("hiEvtPlane") )) ),
	centralityToken_( consumes<int>(iConfig.getParameter<edm::InputTag>("centrality_")) )
{
	edm::Service<TFileService> fs;

	hCent_v1 = fs->make<TH1D>("hCent_v1", "hCent_v1", 200, 0, 200);
	hCent_v2 = fs->make<TH1D>("hCent_v2", "hCent_v2", 200, 0, 200);
	hCent_v3 = fs->make<TH1D>("hCent_v3", "hCent_v3", 200, 0, 200);
	hQ2_v1 = fs->make<TH1D>("hQ2_v1", "hQ2_v1", 1000, 0.0, 1.0);
	hQ2_v2 = fs->make<TH1D>("hQ2_v2", "hQ2_v2", 1000, 0.0, 1.0);
	hQ2_v3 = fs->make<TH1D>("hQ2_v3", "hQ2_v3", 1000, 0.0, 1.0);

}

void QWQ2Trig::fillDescriptions(edm::ConfigurationDescriptions& descriptions)
{
	return;
}

QWQ2Trig::~QWQ2Trig()
{
}

void QWQ2Trig::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	edm::Handle<int> ch;
	iEvent.getByToken(centralityToken_,ch);
	int bin = *(ch.product());

	int RunId = iEvent.id().run();

	edm::Handle<reco::EvtPlaneCollection> epCollection;
	iEvent.getByToken(epToken_, epCollection);
	const reco::EvtPlaneCollection * ep = epCollection.product();
	if ( ! epCollection.isValid() ) return;

	double q2 = (*ep)[8].vn(0);

	if ( RunId < 262777 ) {
		hCent_v1->Fill(bin);
		hQ2_v1->Fill(q2);
	} else if ( RunId < 263212 ) {
		hCent_v2->Fill(bin);
		hQ2_v2->Fill(q2);
	} else {
		hCent_v3->Fill(bin);
		hQ2_v3->Fill(q2);
	}
}

void QWQ2Trig::beginJob()
{
}

void QWQ2Trig::endJob()
{
}

DEFINE_FWK_MODULE(QWQ2Trig);
