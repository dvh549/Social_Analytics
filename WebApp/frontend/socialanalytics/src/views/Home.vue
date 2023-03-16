<template id="page-top">
    <div id="wrapper">

        <!-- Sidebar -->
        <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar">

            <!-- Sidebar - Brand -->
            <a class="sidebar-brand d-flex align-items-center justify-content-center">
                <div class="sidebar-brand-icon rotate-n-15">
                    <i class="fas fa-laugh-wink"></i>
                </div>
                <div class="sidebar-brand-text mx-3">Social Analytics</div>
            </a>

            <!-- Divider -->
            <hr class="sidebar-divider my-0">

            <!-- Nav Item - Dashboard -->
            <li class="nav-item active">
                <a class="nav-link" >
                    <i class="fas fa-fw fa-tachometer-alt"></i>
                    <span>Analyze Dashboard</span></a>
            </li>

            <li class="nav-item">
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
                        <h1 class="h3 mb-0 text-gray-800 mt-5">Dashboard</h1>
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

                    <!-- Content Row -->
                    <div class="row">

                        <!-- Content Column -->
                        <div class="col-lg-6 mb-4">

                            <!-- Project Card Example -->
                            <div class="card shadow mb-4">
                                <div class="card-header py-3">
                                    <h6 class="m-0 font-weight-bold text-primary">Projects</h6>
                                </div>
                                <div class="card-body">
                                    <h4 class="small font-weight-bold">Server Migration <span
                                            class="float-right">20%</span></h4>
                                    <div class="progress mb-4">
                                        <div class="progress-bar bg-danger" role="progressbar" style="width: 20%"
                                            aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
                                    </div>
                                    <h4 class="small font-weight-bold">Sales Tracking <span
                                            class="float-right">40%</span></h4>
                                    <div class="progress mb-4">
                                        <div class="progress-bar bg-warning" role="progressbar" style="width: 40%"
                                            aria-valuenow="40" aria-valuemin="0" aria-valuemax="100"></div>
                                    </div>
                                    <h4 class="small font-weight-bold">Customer Database <span
                                            class="float-right">60%</span></h4>
                                    <div class="progress mb-4">
                                        <div class="progress-bar" role="progressbar" style="width: 60%"
                                            aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"></div>
                                    </div>
                                    <h4 class="small font-weight-bold">Payout Details <span
                                            class="float-right">80%</span></h4>
                                    <div class="progress mb-4">
                                        <div class="progress-bar bg-info" role="progressbar" style="width: 80%"
                                            aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"></div>
                                    </div>
                                    <h4 class="small font-weight-bold">Account Setup <span
                                            class="float-right">Complete!</span></h4>
                                    <div class="progress">
                                        <div class="progress-bar bg-success" role="progressbar" style="width: 100%"
                                            aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                                    </div>
                                </div>
                            </div>


                        </div> 

                        <div class="col-lg-6 mb-4">

                            <!-- Illustrations -->
                            <div class="card shadow mb-4">
                                <div class="card-header py-3">
                                    <h6 class="m-0 font-weight-bold text-primary">Illustrations</h6>
                                </div>
                                <div class="card-body">
                                    <div class="text-center">
                                        <img class="img-fluid px-3 px-sm-4 mt-3 mb-4" style="width: 25rem;"
                                            src="img/undraw_posting_photo.svg" alt="...">
                                    </div>
                                    <p>Add some quality, svg illustrations to your project courtesy of <a
                                            target="_blank" rel="nofollow" href="https://undraw.co/">unDraw</a>, a
                                        constantly updated collection of beautiful svg images that you can use
                                        completely free and without attribution!</p>
                                    <a target="_blank" rel="nofollow" href="https://undraw.co/">Browse Illustrations on
                                        unDraw &rarr;</a>
                                </div>
                            </div>

                            <!-- Approach -->
                            <div class="card shadow mb-4">
                                <div class="card-header py-3">
                                    <h6 class="m-0 font-weight-bold text-primary">Development Approach</h6>
                                </div>
                                <div class="card-body">
                                    <p>SB Admin 2 makes extensive use of Bootstrap 4 utility classes in order to reduce
                                        CSS bloat and poor page performance. Custom CSS classes are used to create
                                        custom components and custom utility classes.</p>
                                    <p class="mb-0">Before working with this theme, you should become familiar with the
                                        Bootstrap framework, especially the utility classes.</p>
                                </div>
                            </div>

                        </div>
                    </div>

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

    <!-- Scroll to Top Button-->
    <a class="scroll-to-top rounded" href="#page-top">
        <i class="fas fa-angle-up"></i>
    </a>

    <!-- Logout Modal-->
    <div class="modal fade" id="logoutModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Ready to Leave?</h5>
                    <button class="close" type="button" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">×</span>
                    </button>
                </div>
                <div class="modal-body">Select "Logout" below if you are ready to end your current session.</div>
                <div class="modal-footer">
                    <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
                    <a class="btn btn-primary" href="login.html">Logout</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import axios from "axios";
import CorrWfh from "../components/corr_wfh.vue"
import CorrWfo from "../components/corr_wfo.vue"
import ClustWfh from "../components/clust_wfh.vue"
import ClustWfo from "../components/clust_wfo.vue"


export default {
  data() {
      return {
        BurnOutDict:{"Female":{"Product":{"No":0,"Yes":0},"Service":{"No":0,"Yes":0}},"Male":{"Product":{"No":0,"Yes":0},"Service":{"No":0,"Yes":0}}},
        corrClust:"corr_yes",
        corr_yes: [],
        corr_no: [],
        clust_yes: [],
        clust_no: [],
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
  },
  methods:{
    routeChange(){
      this.$router.push({name: 'live'});
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
  }
}
</script>
