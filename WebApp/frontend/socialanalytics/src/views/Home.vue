<template id="page-top">
    <div id="wrapper">

        <!-- Sidebar -->
        <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar">

            <!-- Sidebar - Brand -->
            <a class="sidebar-brand d-flex align-items-center justify-content-center">
                <div class="sidebar-brand-icon rotate-n-15">
                    <i class="fas fa-laugh-wink"></i>
                </div>
                <div class="sidebar-brand-text mx-3">CoronaVision</div>
            </a>

            <!-- Divider -->
            <hr class="sidebar-divider my-0">

            <!-- Nav Item - Dashboard -->
            <li class="nav-item active">
                <a class="nav-link" >
                    <i class="fas fa-fw fa-tachometer-alt"></i>
                    <span>Analyze Dashboard</span></a>
            </li>

            <li class="nav-item" @click="routeChange()">
                <a class="nav-link">
                    <i class="fas fa-fw fa-tachometer-alt"></i>
                    <span>Live Dashboard</span></a>
            </li>
        </ul>
        <!-- End of Sidebar -->

        <!-- Content Wrapper -->
        <div id="content-wrapper" class="d-flex flex-column">

            <!-- Main Content -->
            <div id="content">

                <!-- Topbar -->
                
                <!-- End of Topbar -->

                <!-- Begin Page Content -->
                <div class="container-fluid" >

                    <!-- Page Heading -->
                    <div class="d-sm-flex align-items-center justify-content-between mb-4">
                        <h1 class="h3 mb-0 text-gray-800 mt-5">CoronaVision Main Dashboard</h1>
                        <!-- <a href="#" class="d-none d-sm-inline-block btn btn-sm btn-primary shadow-sm mt-5"><i
                                class="fas fa-download fa-sm text-white-50"></i> Generate Report</a> -->
                    </div>

                    <!-- Content Row -->
                    <div class = "row mb-3">
                      <div class ="col">
                         <h4 class="h3 mb-0 text-gray-800 mt-5">Female Burnout Prediction</h4>
                      </div>
                    </div>
                    <div class="row">
                        <!-- Female- Card Example -->
                        <div class="col-xl-3 col-md-2 mb-4">
                            <div class="card border-left-primary shadow h-100 py-2">
                                <div class="card-body">
                                    <div class="row no-gutters align-items-center">
                                        <div class="col mr-2">
                                            <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">
                                                 Company Type: Product (WFH Setup - No)</div>
                                            <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.BurnOutDict["Female"]["Product"]["No"]}}</div>
                                        </div>
                                        <div class="col-auto">
                                            <i class="fas fa-calendar fa-2x text-gray-300"></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Earnings (Monthly) Card Example -->
                        <div class="col-xl-3 col-md-2 mb-4">
                            <div class="card border-left-success shadow h-100 py-2">
                                <div class="card-body">
                                    <div class="row no-gutters align-items-center">
                                        <div class="col mr-2">
                                            <div class="text-xs font-weight-bold text-success text-uppercase mb-1">
                                                Company Type: Product (WFH Setup - Yes)</div>
                                            <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.BurnOutDict["Female"]["Product"]["Yes"]}}</div>
                                        </div>
                                        <div class="col-auto">
                                            <i class="fas fa-dollar-sign fa-2x text-gray-300"></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="col-xl-3 col-md-2 mb-4">
                            <div class="card border-left-warning shadow h-100 py-2">
                                <div class="card-body">
                                    <div class="row no-gutters align-items-center">
                                        <div class="col mr-2">
                                            <div class="text-xs font-weight-bold text-warning text-uppercase mb-1">
                                                  Company Type: Service (WFH Setup - No)</div>
                                            <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.BurnOutDict["Female"]["Service"]["No"]}}</div>
                                        </div>
                                        <div class="col-auto">
                                            <i class="fas fa-comments fa-2x text-gray-300"></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Pending Requests Card Example -->
                        <div class="col-xl-3 col-md-2 mb-4">
                            <div class="card border-left-info shadow h-100 py-2">
                                <div class="card-body">
                                    <div class="row no-gutters align-items-center">
                                        <div class="col mr-2">
                                            <div class="text-xs font-weight-bold text-info text-uppercase mb-1">
                                                Company Type: Service (WFH Setup - No)</div>
                                            <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.BurnOutDict["Female"]["Service"]["Yes"]}}</div>
                                        </div>
                                        <div class="col-auto">
                                            <i class="fas fa-comments fa-2x text-gray-300"></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                    </div>

                     <div class = "row mb-3">
                      <div class ="col">
                         <h4 class="h3 mb-0 text-gray-800 mt-5">Male Burnout Prediction</h4>
                      </div>
                    </div>
                    <div class="row">
                        <!-- Female- Card Example -->
                        <div class="col-xl-3 col-md-2 mb-4">
                            <div class="card border-left-primary shadow h-100 py-2">
                                <div class="card-body">
                                    <div class="row no-gutters align-items-center">
                                        <div class="col mr-2">
                                            <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">
                                                 Company Type: Product (WFH Setup - No)</div>
                                            <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.BurnOutDict["Male"]["Product"]["No"]}}</div>
                                        </div>
                                        <div class="col-auto">
                                            <i class="fas fa-calendar fa-2x text-gray-300"></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Earnings (Monthly) Card Example -->
                        <div class="col-xl-3 col-md-2 mb-4">
                            <div class="card border-left-success shadow h-100 py-2">
                                <div class="card-body">
                                    <div class="row no-gutters align-items-center">
                                        <div class="col mr-2">
                                            <div class="text-xs font-weight-bold text-success text-uppercase mb-1">
                                                Company Type: Product (WFH Setup - Yes)</div>
                                            <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.BurnOutDict["Male"]["Product"]["Yes"]}}</div>
                                        </div>
                                        <div class="col-auto">
                                            <i class="fas fa-dollar-sign fa-2x text-gray-300"></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="col-xl-3 col-md-2 mb-4">
                            <div class="card border-left-warning shadow h-100 py-2">
                                <div class="card-body">
                                    <div class="row no-gutters align-items-center">
                                        <div class="col mr-2">
                                            <div class="text-xs font-weight-bold text-warning text-uppercase mb-1">
                                                  Company Type: Service (WFH Setup - No)</div>
                                            <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.BurnOutDict["Male"]["Service"]["No"]}}</div>
                                        </div>
                                        <div class="col-auto">
                                            <i class="fas fa-comments fa-2x text-gray-300"></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Pending Requests Card Example -->
                        <div class="col-xl-3 col-md-2 mb-4">
                            <div class="card border-left-info shadow h-100 py-2">
                                <div class="card-body">
                                    <div class="row no-gutters align-items-center">
                                        <div class="col mr-2">
                                            <div class="text-xs font-weight-bold text-info text-uppercase mb-1">
                                                Company Type: Service (WFH Setup - No)</div>
                                            <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.BurnOutDict["Male"]["Service"]["Yes"]}}</div>
                                        </div>
                                        <div class="col-auto">
                                            <i class="fas fa-comments fa-2x text-gray-300"></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                    </div>
                    <div class = "row mb-3">
                      <div class ="col">
                         <h4 class="h3 mb-0 text-gray-800 mt-5">Correlation And Clustering</h4>
                      </div>
                    </div>
                    <!-- Content Row -->
                    <div class="row">
                      <div class="col">
                        <ul class="nav nav-tabs center">
                          <li class="nav-item">
                            <a class="nav-link active" id="corr_yes" @click="changePage('corr_yes')">Corr_WFH</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="corr_no" @click="changePage('corr_no')">Corr_WFO</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="clust_yes" @click="changePage('clust_yes')">Cluster 0</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="clust_no" @click="changePage('clust_no')">Cluster 1</a>
                          </li>
                        </ul>
                      </div>
                    </div>
                    <div class="row">
                      <CorrWfh v-if="corrClust=='corr_yes'"
                        :options="options"
                        :corr_yes="corr_yes"/>

                      <CorrWfo v-if="corrClust=='corr_no'"
                        :options="options"
                        :corr_yes="corr_no"/>
                        
                      <ClustWfh v-if="corrClust=='clust_yes'"
                        :options="options"
                        :corr_yes="clust_yes"/>

                      <ClustWfo v-if="corrClust=='clust_no'"
                        :options="options"
                        :corr_yes="clust_no"/>

                    </div>
                    <div class = "row mb-3">
                      <div class ="col">
                         <h4 class="h3 mb-0 text-gray-800 mt-5">Overall SG Sentiment</h4>
                      </div>
                    </div>
                    <!-- <div class="row">
                      <div class="col">
                        <ul class="nav nav-tabs center">
                          <li class="nav-item">
                            <a class="nav-link active" id="senti_sg" @click="changeSentiPage('senti_sg')">Singapore</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="senti_us" @click="changeSentiPage('senti_us')">United State</a>
                          </li>
                        </ul>
                      </div>
                    </div> -->
                    <div class="row" >
                      <div class="col">
                        <ul class="nav nav-tabs center">
                          <li class="nav-item">
                            <a class="nav-link active" id="start" @click="changeSentiTimePage('start')">Start</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="cb" @click="changeSentiTimePage('cb')">Circuit Breaker</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="phase" @click="changeSentiTimePage('phase')">Phases</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="acuterPhase" @click="changeSentiTimePage('acuterPhase')">Acute Phases</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="dorsconGreen" @click="changeSentiTimePage('dorsconGreen')">Dorscon Green</a>
                          </li>
                        </ul>
                      </div>
                    </div>
                    
                    <!-- <div class="row"  > -->
                      <SGStartSenti v-if="sentiTimePage=='start'" />
                      <SGCBSenti v-if=" sentiTimePage=='cb'" />
                      <SGPhasesSenti v-if=" sentiTimePage=='phase'" />
                      <SGAcuteSenti v-if="sentiTimePage=='acuterPhase'" />
                      <SGGreenSenti v-if="sentiTimePage=='dorsconGreen'" />
                    <div class = "row mb-3">
                      <div class ="col">
                         <h4 class="h3 mb-0 text-gray-800 mt-5">Overall US Sentiment</h4>
                      </div>
                    </div>
                    <div class="row" >
                      <div class="col">
                        <ul class="nav nav-tabs center">
                          <li class="nav-item">
                            <a class="nav-link active" id="start2" @click="changeSentiTimePage2('start2')">Start</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="lockdown" @click="changeSentiTimePage2('lockdown')">Lockdown</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="Y20" @click="changeSentiTimePage2('Y20')">Year 2020</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="Y21" @click="changeSentiTimePage2('Y21')">Year 2021</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="Y22" @click="changeSentiTimePage2('Y22')">Year 2022</a>
                          </li>
                        </ul>
                      </div>
                    </div>
                      <USStartSenti v-if="sentiTimePage2=='start2'" />
                      <USCBSenti v-if="sentiTimePage2=='lockdown'" />
                      <USPhasesSenti v-if="sentiTimePage2=='Y20'" />
                      <USAcuteSenti v-if="sentiTimePage2=='Y21'" />
                      <USGreenSenti v-if="sentiTimePage2=='Y22'" />

                    
                    
                    <div class = "row mb-3">
                      <div class ="col">
                         <h4 class="h3 mb-0 text-gray-800 mt-5">Overall SG Topic And Sentiment</h4>
                      </div>
                    </div>
                    <div class="row" >
                      <div class="col">
                        <ul class="nav nav-tabs center">
                          <li class="nav-item">
                            <a class="nav-link active" id="start_topic" @click="changeTopicTimePage('start_topic')">Start</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="cb_topic" @click="changeTopicTimePage('cb_topic')">Circuit Breaker</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="phase_topic" @click="changeTopicTimePage('phase_topic')">Phases</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="acuterPhase_topic" @click="changeTopicTimePage('acuterPhase_topic')">Acute Phases</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="dorsconGreen_topic" @click="changeTopicTimePage('dorsconGreen_topic')">Dorscon Green</a>
                          </li>
                        </ul>
                      </div>
                    </div>
                        <TopicStartSG  v-if="sg_topic=='start_topic'"/>
                        <TopicCBSG  v-if="sg_topic=='cb_topic'"/>
                        <TopicPhaseSG  v-if="sg_topic=='phase_topic'"/>
                        <TopicAcuteSG  v-if="sg_topic=='acuterPhase_topic'"/>
                        <TopicGreenSG  v-if="sg_topic=='dorsconGreen_topic'"/>
                    
                    <div class = "row mb-3">
                      <div class ="col">
                         <h4 class="h3 mb-0 text-gray-800 mt-5">Overall US Topic And Sentiment</h4>
                      </div>
                    </div>
                    <div class="row" >
                      <div class="col">
                        <ul class="nav nav-tabs center">
                          <li class="nav-item">
                            <a class="nav-link active" id="start_topic_us" @click="changeTopicTimePage2('start_topic_us')">Start</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="cb_topic_us" @click="changeTopicTimePage2('cb_topic_us')">Lockdown</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="phase_topic_us" @click="changeTopicTimePage2('phase_topic_us')">Year 2020</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="acuterPhase_topic_us" @click="changeTopicTimePage2('acuterPhase_topic_us')">Year 2021</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="dorsconGreen_topic_us" @click="changeTopicTimePage2('dorsconGreen_topic_us')">year 2022</a>
                          </li>
                        </ul>
                      </div>
                    </div>
                        <TopicStartUS  v-if="us_topic=='start_topic_us'"/>
                        <TopicCBUS  v-if="us_topic=='cb_topic_us'"/>
                        <TopicPhaseUS  v-if="us_topic=='phase_topic_us'"/>
                        <TopicAcuteUS  v-if="us_topic=='acuterPhase_topic_us'"/>
                        <TopicGreenUS  v-if="us_topic=='dorsconGreen_topic_us'"/>

                    <div class = "row mb-3">
                      <div class ="col">
                         <h4 class="h3 mb-0 text-gray-800 mt-5">SG Quote/Reply Network</h4>
                      </div>
                    </div>
                    <div class="row" >
                      <div class="col">
                        <ul class="nav nav-tabs center">
                          <li class="nav-item">
                            <a class="nav-link active" id="start_social_sg" @click="changeSocialSG('start_social_sg')">"Covid" Quote Network</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="cb_social_sg" @click="changeSocialSG('cb_social_sg')">"Covid" Reply Network</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="phase_social_sg" @click="changeSocialSG('phase_social_sg')">"Coronavirus" Quote Network</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="acuterPhase_social_sg" @click="changeSocialSG('acuterPhase_social_sg')">"Coronavirus" Reply Network</a>
                          </li>
                        </ul>
                      </div>
                    </div> 
                    <SocialCovidQuote v-if="sg_social=='start_social_sg'"/>
                    <SocialCovidReply v-if="sg_social=='cb_social_sg'"/>
                    <SocialCoronaQuote v-if="sg_social=='phase_social_sg'"/>
                    <SocialCoronaReply v-if="sg_social=='acuterPhase_social_sg'"/>

                   <div class = "row mb-3">
                      <div class ="col">
                         <h4 class="h3 mb-0 text-gray-800 mt-5">US Quote/Reply Network</h4>
                      </div>
                    </div>
                    <div class="row" >
                      <div class="col">
                        <ul class="nav nav-tabs center">
                          <li class="nav-item">
                            <a class="nav-link active" id="start_social_us" @click="changeSocialUS('start_social_us')"> Quote Network</a>
                          </li>
                          <li class="nav-item">
                            <a class="nav-link" id="cb_social_us" @click="changeSocialUS('cb_social_us')">Reply Network</a>
                          </li>
                  
                        </ul>
                      </div>
                    </div> 
                    <SocialCovidQuoteUS v-if="us_social=='start_social_us'"/>
                    <SocialCovidReplyUS v-if="us_social=='cb_social_us'"/>

                </div>
                <!-- /.container-fluid -->

            </div>
            <!-- End of Main Content -->

            <!-- Footer -->
            <footer class="sticky-footer bg-white">
                <div class="container my-auto">
                    <div class="copyright text-center my-auto">
                        <span>Copyright &copy; HELLO WORLD 2023</span>
                    </div>
                </div>
            </footer>
            <!-- End of Footer -->

        </div>
        <!-- End of Content Wrapper -->

    </div>
    <!-- End of Page Wrapper -->

  
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import axios from "axios";
import CorrWfh from "../components/corr_wfh.vue"
import CorrWfo from "../components/corr_wfo.vue"
import ClustWfh from "../components/clust_wfh.vue"
import ClustWfo from "../components/clust_wfo.vue"
import SGStartSenti from "../components/sg_start_senti.vue"
import SGCBSenti from "../components/sg_cb_senti.vue"
import SGPhasesSenti from "../components/sg_phases_senti.vue"
import SGAcuteSenti from "../components/sg_acutePhases_senti.vue"
import SGGreenSenti from "../components/sg_green_senti.vue"
import USStartSenti from "../components/us_start_senti.vue"
import USCBSenti from "../components/us_cb_senti.vue"
import USPhasesSenti from "../components/us_phases_senti.vue"
import USAcuteSenti from "../components/us_acutePhases_senti.vue"
import USGreenSenti from "../components/us_green_senti.vue"
import TopicStartSG from "../components/topic_start_sg.vue"
import TopicCBSG from "../components/topic_cb_sg.vue"
import TopicPhaseSG from "../components/topic_phases_sg.vue"
import TopicAcuteSG from "../components/topic_acute_sg.vue"
import TopicGreenSG from "../components/topic_green_sg.vue"
import TopicStartUS from "../components/topic_start_us.vue"
import TopicCBUS from "../components/topic_cb_us.vue"
import TopicPhaseUS from "../components/topic_phases_us.vue"
import TopicAcuteUS from "../components/topic_acute_us.vue"
import TopicGreenUS from "../components/topic_green_us.vue"
import SocialCovidQuote from "../components/covid_quote_network_sg.vue"
import SocialCovidReply from "../components/covid_reply_network_sg.vue"
import SocialCoronaQuote from "../components/corona_quote_network_sg.vue"
import SocialCoronaReply from "../components/corona_reply_network_sg.vue"
import SocialCovidQuoteUS from "../components/covid_quote_network_us.vue"
import SocialCovidReplyUS from "../components/covid_reply_network_us.vue"

export default {
  data() {
      return {
        us_social:"start_social_us",
        sg_social:"start_social_sg",
        us_topic:"start_topic_us",
        sg_topic:"start_topic",
        BurnOutDict:{"Female":{"Product":{"No":0,"Yes":0},"Service":{"No":0,"Yes":0}},"Male":{"Product":{"No":0,"Yes":0},"Service":{"No":0,"Yes":0}}},
        corrClust:"corr_yes",
        // sentiPage:"senti_sg",
        // sentiPage:"senti_sg",
        sentiTimePage2:"start2",
        sentiTimePage:"start",
        corr_yes: [],
        corr_no: [],
        clust_yes: [],
        clust_no: [],
        start_vis_sg:"../components/sg_start_lda_vis_tuned_18.html",
        externalHtml:'',
        // positiveWords:[],
        // negativeWords:[],
        // neutralWords:[],
        options: {
            chart: {
              height: 350,
              type: 'heatmap',
            },
            dataLabels: {
              enabled: true,
              style: {
                colors:["#000000"]
              }
            },
            colors: ["#008FFB"],
            // title: {
            //   text: 'Correlation Work From Home'
            // },
          },
      }
    },
  components:{
    CorrWfh,
    CorrWfo,
    ClustWfh,
    ClustWfo,
    SGStartSenti,
    SGCBSenti,
    SGPhasesSenti,
    SGAcuteSenti,
    SGGreenSenti,
    USStartSenti,
    USCBSenti,
    USPhasesSenti,
    USAcuteSenti,
    USGreenSenti,
    TopicStartSG,
    TopicCBSG,
    TopicPhaseSG,
    TopicAcuteSG,
    TopicGreenSG,
    TopicStartUS,
    TopicCBUS,
    TopicPhaseUS,
    TopicAcuteUS,
    TopicGreenUS,
    SocialCovidQuote,
    SocialCovidReply,
    SocialCoronaQuote,
    SocialCoronaReply,
    SocialCovidQuoteUS,
    SocialCovidReplyUS
  },
  methods:{
    routeChange(){
      this.$router.push({name: 'LiveAnalysis'});
    },
    changeSocialUS(val){
        this.us_social= val
        console.log(this.us_social)
         if(val=="start_social_us"){
              document.getElementById("start_social_us").className="nav-link active"
              document.getElementById("cb_social_us").className="nav-link"
           }else if(val=="cb_social_us"){
          
              document.getElementById("start_social_us").className="nav-link"
              document.getElementById("cb_social_us").className="nav-link  active"
           }
    },
    changePage(val){
      this.corrClust= val
      if (val=="corr_yes"){
        document.getElementById("corr_yes").className="nav-link active"
        document.getElementById("corr_no").className="nav-link"
        document.getElementById("clust_yes").className="nav-link"
        document.getElementById("clust_no").className="nav-link"
      }else if(val=="corr_no"){
        document.getElementById("corr_yes").className="nav-link"
        document.getElementById("corr_no").className="nav-link active"
        document.getElementById("clust_yes").className="nav-link"
        document.getElementById("clust_no").className="nav-link"
      }
      else if(val=="clust_yes"){
        document.getElementById("corr_yes").className="nav-link"
        document.getElementById("corr_no").className="nav-link"
        document.getElementById("clust_yes").className="nav-link active"
        document.getElementById("clust_no").className="nav-link"
      }else{
        document.getElementById("corr_yes").className="nav-link"
        document.getElementById("corr_no").className="nav-link"
        document.getElementById("clust_yes").className="nav-link"
        document.getElementById("clust_no").className="nav-link active"
      }
    },
    changeSentiPage(val){
      this.sentiPage= val
      if (val=="senti_sg"){
        document.getElementById("senti_sg").className="nav-link active"
        document.getElementById("senti_us").className="nav-link"
      }else{
        this.sentiTimePage= 'start2'
        document.getElementById("senti_sg").className="nav-link"
        document.getElementById("senti_us").className="nav-link active"

        document.getElementById("start").className="nav-link"
        document.getElementById("cb").className="nav-link"
        document.getElementById("phase").className="nav-link"
        document.getElementById("acuterPhase").className="nav-link"
        document.getElementById("dorsconGreen").className="nav-link"
        document.getElementById("start2").className="nav-link active"
        document.getElementById("lockdown").className="nav-link"
        document.getElementById("Y20").className="nav-link"
        document.getElementById("Y21").className="nav-link"
        document.getElementById("Y22").className="nav-link"
      }
    },
    changeSentiTimePage(val){
      this.sentiTimePage= val
        if (val=="start"){
          document.getElementById("start").className="nav-link active"
          document.getElementById("cb").className="nav-link"
          document.getElementById("phase").className="nav-link"
          document.getElementById("acuterPhase").className="nav-link"
          document.getElementById("dorsconGreen").className="nav-link"
        


        }else if(val=="cb"){
          document.getElementById("start").className="nav-link"
          document.getElementById("cb").className="nav-link active"
          document.getElementById("phase").className="nav-link"
          document.getElementById("acuterPhase").className="nav-link"
          document.getElementById("dorsconGreen").className="nav-link"
          
        }
        else if(val=="phase"){
          document.getElementById("start").className="nav-link"
          document.getElementById("cb").className="nav-link"
          document.getElementById("phase").className="nav-link active"
          document.getElementById("acuterPhase").className="nav-link"
          document.getElementById("dorsconGreen").className="nav-link"
          
        }else if(val=="acuterPhase"){
          document.getElementById("start").className="nav-link"
          document.getElementById("cb").className="nav-link"
          document.getElementById("phase").className="nav-link"
          document.getElementById("acuterPhase").className="nav-link active"
          document.getElementById("dorsconGreen").className="nav-link"
          
        }else if(val=="dorsconGreen"){
          document.getElementById("start").className="nav-link"
          document.getElementById("cb").className="nav-link"
          document.getElementById("phase").className="nav-link"
          document.getElementById("acuterPhase").className="nav-link"
          document.getElementById("dorsconGreen").className="nav-link active"
          
        }
      },
      changeSentiTimePage2(val){
        this.sentiTimePage2= val

        if(val=="start2"){
          document.getElementById("start2").className="nav-link active"
          document.getElementById("lockdown").className="nav-link"
          document.getElementById("Y20").className="nav-link"
          document.getElementById("Y21").className="nav-link"
          document.getElementById("Y22").className="nav-link"
        }else if(val=="lockdown"){
          
          document.getElementById("start2").className="nav-link"
          document.getElementById("lockdown").className="nav-link active"
          document.getElementById("Y20").className="nav-link"
          document.getElementById("Y21").className="nav-link"
          document.getElementById("Y22").className="nav-link"
        }else if(val=="Y20"){
          
          document.getElementById("start2").className="nav-link"
          document.getElementById("lockdown").className="nav-link"
          document.getElementById("Y20").className="nav-link active"
          document.getElementById("Y21").className="nav-link"
          document.getElementById("Y22").className="nav-link"
        }else if(val=="Y21"){
          
          document.getElementById("start2").className="nav-link"
          document.getElementById("lockdown").className="nav-link"
          document.getElementById("Y20").className="nav-link"
          document.getElementById("Y21").className="nav-link active"
          document.getElementById("Y22").className="nav-link"
        }else if(val=="Y22"){
          
          document.getElementById("start2").className="nav-link"
          document.getElementById("lockdown").className="nav-link"
          document.getElementById("Y20").className="nav-link"
          document.getElementById("Y21").className="nav-link"
          document.getElementById("Y22").className="nav-link active"
        }
      },
      changeTopicTimePage(val){
        this.sg_topic= val
        console.log(this.sg_topic)
         if(val=="start_topic"){
          document.getElementById("start_topic").className="nav-link active"
          document.getElementById("cb_topic").className="nav-link"
          document.getElementById("phase_topic").className="nav-link"
          document.getElementById("acuterPhase_topic").className="nav-link"
          document.getElementById("dorsconGreen_topic").className="nav-link"
        }else if(val=="cb_topic"){
          
         document.getElementById("start_topic").className="nav-link"
          document.getElementById("cb_topic").className="nav-link  active"
          document.getElementById("phase_topic").className="nav-link"
          document.getElementById("acuterPhase_topic").className="nav-link"
          document.getElementById("dorsconGreen_topic").className="nav-link"
        }else if(val=="phase_topic"){
          
          document.getElementById("start_topic").className="nav-link"
          document.getElementById("cb_topic").className="nav-link"
          document.getElementById("phase_topic").className="nav-link active"
          document.getElementById("acuterPhase_topic").className="nav-link"
          document.getElementById("dorsconGreen_topic").className="nav-link"
        }else if(val=="acuterPhase_topic"){
          
          document.getElementById("start_topic").className="nav-link"
          document.getElementById("cb_topic").className="nav-link"
          document.getElementById("phase_topic").className="nav-link"
          document.getElementById("acuterPhase_topic").className="nav-link active"
          document.getElementById("dorsconGreen_topic").className="nav-link"
        }else if(val=="dorsconGreen_topic"){
          
          document.getElementById("start_topic").className="nav-link"
          document.getElementById("cb_topic").className="nav-link"
          document.getElementById("phase_topic").className="nav-link"
          document.getElementById("acuterPhase_topic").className="nav-link"
          document.getElementById("dorsconGreen_topic").className="nav-link active"
        }

      },
      changeSocialSG(val){
        this.sg_social= val
        console.log(this.sg_topic)
         if(val=="start_social_sg"){
              document.getElementById("start_social_sg").className="nav-link active"
              document.getElementById("cb_social_sg").className="nav-link"
              document.getElementById("phase_social_sg").className="nav-link"
              document.getElementById("acuterPhase_social_sg").className="nav-link"
           }else if(val=="cb_social_sg"){
          
              document.getElementById("start_social_sg").className="nav-link"
              document.getElementById("cb_social_sg").className="nav-link  active"
              document.getElementById("phase_social_sg").className="nav-link"
              document.getElementById("acuterPhase_social_sg").className="nav-link"
           }else if(val=="phase_social_sg"){
          
              document.getElementById("start_social_sg").className="nav-link"
              document.getElementById("cb_social_sg").className="nav-link"
              document.getElementById("phase_social_sg").className="nav-link active"
              document.getElementById("acuterPhase_social_sg").className="nav-link"
          }else if(val=="acuterPhase_topic"){
          
          document.getElementById("start_social_sg").className="nav-link"
          document.getElementById("phase_social_sg").className="nav-link"
          document.getElementById("phase_social_sg").className="nav-link"
          document.getElementById("acuterPhase_social_sg").className="nav-link active"
           }

      },
      changeTopicTimePage2(val){
        this.us_topic= val
        console.log(this.sg_topic)
         if(val=="start_topic"){
          document.getElementById("start_topic_us").className="nav-link active"
          document.getElementById("cb_topic_us").className="nav-link"
          document.getElementById("phase_topic_us").className="nav-link"
          document.getElementById("acuterPhase_topic_us").className="nav-link"
          document.getElementById("dorsconGreen_topic_us").className="nav-link"
        }else if(val=="cb_topic"){
          
         document.getElementById("start_topic_us").className="nav-link"
          document.getElementById("cb_topic_us").className="nav-link  active"
          document.getElementById("phase_topic_us").className="nav-link"
          document.getElementById("acuterPhase_topic_us").className="nav-link"
          document.getElementById("dorsconGreen_topic_us").className="nav-link"
        }else if(val=="phase_topic"){
          
          document.getElementById("start_topic_us").className="nav-link"
          document.getElementById("cb_topic_us").className="nav-link"
          document.getElementById("phase_topic_us").className="nav-link active"
          document.getElementById("acuterPhase_topic_us").className="nav-link"
          document.getElementById("dorsconGreen_topic_us").className="nav-link"
        }else if(val=="acuterPhase_topic"){
          
          document.getElementById("start_topic_us").className="nav-link"
          document.getElementById("cb_topic_us").className="nav-link"
          document.getElementById("phase_topic_us").className="nav-link"
          document.getElementById("acuterPhase_topic_us").className="nav-link active"
          document.getElementById("dorsconGreen_topic_us").className="nav-link"
        }else if(val=="dorsconGreen_topic"){
          
          document.getElementById("start_topic_us").className="nav-link"
          document.getElementById("cb_topic_us").className="nav-link"
          document.getElementById("phase_topic_us").className="nav-link"
          document.getElementById("acuterPhase_topic_us").className="nav-link"
          document.getElementById("dorsconGreen_topic_us").className="nav-link active"
        }

      }


  },
  
  mounted(){
    console.log("HERE")
    axios.get("http://127.0.0.1:5000/getBurnOut")
      .then(res=>{
        console.log(res)
        this.BurnOutDict = res.data.message
      })
    axios.get("http://127.0.0.1:5000/getClustering")
      .then(res=>{
        // console.log(res.data)
        // console.log(res.data.message.clust_no)
        this.corr_yes = res.data.message.corr_yes
        this.corr_no = res.data.message.corr_no
        this.clust_yes = res.data.message.clust_yes
        this.clust_no = res.data.message.clust_no
      })
    // axios.get("http://127.0.0.1:5000/getSentimentAnalysis")
    //   .then(res=>{
    //     // console.log(res.data)
    //     // console.log(res.data.message.wordCloud.positive)
    //     this.positiveWords= res.data.message.wordCloud.positive
    //     this.negativeWords= res.data.message.wordCloud.negative
    //     this.neutralWords= res.data.message.wordCloud.neutral
    //     console.log(this.positiveWords)
    //     console.log(this.negativeWords)
    //     console.log(this.neutralWords)

    //   })
  }
}
</script>
