<template>
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
            <li class="nav-item" @click="routeChange()">
                <a class="nav-link" >
                    <i class="fas fa-fw fa-tachometer-alt"></i>
                    <span>Analyze Dashboard</span></a>
            </li>

            <li class="nav-item active">
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
                     <div class="d-sm-flex align-items-center justify-content-between mb-4">
                        <h1 class="h3 mb-0 text-gray-800 mt-5">CoronaVision Live Dashboard</h1>
                        <!-- <a href="#" class="d-none d-sm-inline-block btn btn-sm btn-primary shadow-sm mt-5"><i
                                class="fas fa-download fa-sm text-white-50"></i> Generate Report</a> -->
                    </div>
                    <div class = "row mb-3">
                      <div class ="col">
                         <h4 class="h3 mb-0 text-gray-800 mt-5">Burnout Prediction: {{burnOutValue}}</h4>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-xl-4 col-md-2 mb-4">
                            <div class="card border-left-primary shadow h-100 py-2">
                                <div class="card-body">
                                    <div class="row no-gutters align-items-center">
                                        <div class="col mr-2">
                                            <div class="text-s font-weight-bold text-primary text-uppercase mb-1" style="height:80px">
                                                Gender: </div>
                                            <!-- <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.BurnOutDict["Female"]["Product"]["No"]}}</div> -->
                                            <div>
                                              <select class="form-select" v-model="burnoutGender">
                                                    <option value="" selected disabled>Please select an option</option>
                                                    <option value="male">Male</option>
                                                    <option value="female">female</option>
                                                  </select>
                                                  <!-- <p>You selected: {{ selectedOption }}</p> -->
                                                </div>
                                            </div>
                                        </div>
                                      
                                    </div>
                                </div>
                            </div>

                            <div class="col-xl-4 col-md-2 mb-4">
                              <div class="card border-left-primary shadow h-100 py-2">
                                  <div class="card-body">
                                      <div class="row no-gutters align-items-center">
                                          <div class="col mr-2">
                                              <div class="text-s font-weight-bold text-primary text-uppercase mb-1" style="height:80px">
                                                  WFH Setup? </div>
                                              <!-- <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.BurnOutDict["Female"]["Product"]["No"]}}</div> -->
                                              <div>
                                                <select class="form-select" v-model="WFHOptions">
                                                      <option value="" selected disabled>Please select an option</option>
                                                      <option value="yes">yes</option>
                                                      <option value="no">no</option>
                                                    </select>
                                                    <!-- <p>You selected: {{ selectedOption }}</p> -->
                                                  </div>
                                              </div>
                                          </div>
                                        
                                      </div>
                                  </div>
                            </div>

                            <div class="col-xl-4 col-md-2 mb-4">
                              <div class="card border-left-primary shadow h-100 py-2">
                                  <div class="card-body">
                                      <div class="row no-gutters align-items-center">
                                          <div class="col mr-2">
                                              <div class="text-s font-weight-bold text-primary text-uppercase mb-1" style="height:80px">
                                                  Designation: [0-5] The bigger, the higher the designation </div>
                                              <!-- <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.BurnOutDict["Female"]["Product"]["No"]}}</div> -->
                                              <div>
                                                    <select class="form-select" v-model="DesignationOption">
                                                      <option value="" selected disabled>Please select an option</option>
                                                      <option value="0">0</option>
                                                      <option value="1">1</option>
                                                      <option value="2">2</option>
                                                      <option value="3">3</option>
                                                      <option value="4">4</option>
                                                      <option value="5">5</option>
                                                    </select>
                                                    <!-- <p>You selected: {{ selectedOption }}</p> -->
                                                  </div>
                                              </div>
                                          </div>
                                        
                                      </div>
                                  </div>
                            </div>
                            <div class="col-xl-6 col-md-2 mb-4">
                              <div class="card border-left-primary shadow h-100 py-2">
                                  <div class="card-body">
                                      <div class="row no-gutters align-items-center">
                                          <div class="col mr-2">
                                              <div class="text-m font-weight-bold text-primary text-uppercase mb-1" style="height:80px">
                                                  Resource allocation: ([0-10] Amount of resources allocated, higher means more) </div>
                                              <!-- <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.BurnOutDict["Female"]["Product"]["No"]}}</div> -->
                                              <div>
                                                    <select class="form-select" v-model="resourceOption">
                                                      <option value="" selected disabled>Please select an option</option>
                                                      <option value="0">0</option>
                                                      <option value="1">1</option>
                                                      <option value="2">2</option>
                                                      <option value="3">3</option>
                                                      <option value="4">4</option>
                                                      <option value="5">5</option>
                                                      <option value="6">6</option>
                                                      <option value="7">7</option>
                                                      <option value="8">8</option>
                                                      <option value="9">9</option>
                                                      <option value="10">10</option>

                                                    </select>
                                                    <!-- <p>You selected: {{ selectedOption }}</p> -->
                                                  </div>
                                              </div>
                                          </div>
                                        
                                      </div>
                                  </div>
                            </div>

                            <div class="col-xl-6 col-md-2 mb-4">
                              <div class="card border-left-primary shadow h-100 py-2">
                                  <div class="card-body">
                                      <div class="row no-gutters align-items-center">
                                          <div class="col mr-2">
                                              <div class="text-s font-weight-bold text-primary text-uppercase mb-1" style="height:80px">
                                                  Mental Fatigue: ([0.0-10.0] Level of employee's fatigue) </div>
                                              <!-- <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.BurnOutDict["Female"]["Product"]["No"]}}</div> -->
                                              <div>
                                                    <select class="form-select" v-model="mentalOption">
                                                      <option value="" selected disabled>Please select an option</option>
                                                      <option value="0">0</option>
                                                      <option value="1">1</option>
                                                      <option value="2">2</option>
                                                      <option value="3">3</option>
                                                      <option value="4">4</option>
                                                      <option value="5">5</option>
                                                      <option value="6">6</option>
                                                      <option value="7">7</option>
                                                      <option value="8">8</option>
                                                      <option value="9">9</option>
                                                      <option value="10">10</option>
                                                    </select>
                                                    <!-- <p>You selected: {{ selectedOption }}</p> -->
                                                  </div>
                                              </div>
                                          </div>
                                        
                                      </div>
                                  </div>
                            </div>
                            <div class="col-12 mb-2" >
                                <button @click="getBurnOutPrediction" class="btn btn-primary btn-block">Submit</button>
                            </div>

                  </div>
                  <div class = "row mb-2">
                      <div class ="col">
                         <h4 class="h3 mb-0 text-gray-800 mt-5">Fake Or Real? : {{this.classificationResult}} </h4>
                      </div>
                    </div>
                  <div class="row">
                    <div class="col-xl-12 col-md-12 mb-4">
                        <div class="card border-left-primary shadow h-100 py-2">
                            <div class="card-body">
                                <div class="row no-gutters align-items-center">
                                    <div class="col mr-2">
                                        <div class="text-s font-weight-bold text-primary text-uppercase mb-1" >
                                            Enter the text for analysis</div>
                                        <!-- <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.BurnOutDict["Female"]["Product"]["No"]}}</div> -->
                                        <div>
                                            <textarea class="col-12" id="textarea-input" v-model="classificationText" style="height:100px;"></textarea>
                                        </div>
                                    </div>
                                  
                                </div>
                            </div>
                          </div>
                    </div>

                  <div class="col-12 mb-3">
                      <button @click="getClassificationResult" class="btn btn-primary btn-block">Submit</button>
                  </div>
                </div>

              <div class = "row mb-2">
                  <div class="col-xl-3 col-md-3 mb-4">
                        <div class="card border-left-primary shadow h-100 py-2">
                            <div class="card-body">
                                <div class="row no-gutters align-items-center">
                                    <div class="col mr-2">
                                        <div class="text-s font-weight-bold text-primary text-uppercase mb-1" >
                                            Overall Sentiment</div>
                                        <!-- <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.BurnOutDict["Female"]["Product"]["No"]}}</div> -->
                                        <div>
                                            <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.overallSenti}}</div>
                                        </div>
                                    </div>
                                  
                                </div>
                            </div>
                          </div>
                    </div>
                  <div class="col-xl-3 col-md-3 mb-4">
                        <div class="card border-left-primary shadow h-100 py-2">
                            <div class="card-body">
                                <div class="row no-gutters align-items-center">
                                    <div class="col mr-2">
                                        <div class="text-s font-weight-bold text-primary text-uppercase mb-1" >
                                            Top Keywords</div>
                                        <!-- <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.BurnOutDict["Female"]["Product"]["No"]}}</div> -->
                                        <div>
                                            <div class="h5 mb-0 font-weight-bold text-gray-800">{{topWords[0]}}</div>
                                        </div>
                                    </div>
                                  
                                </div>
                            </div>
                          </div>
                    </div>
                  <div class="col-xl-3 col-md-3 mb-4">
                        <div class="card border-left-primary shadow h-100 py-2">
                            <div class="card-body">
                                <div class="row no-gutters align-items-center">
                                    <div class="col mr-2">
                                        <div class="text-s font-weight-bold text-primary text-uppercase mb-1" >
                                            Top Keywords</div>
                                        <!-- <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.BurnOutDict["Female"]["Product"]["No"]}}</div> -->
                                        <div>
                                            <div class="h5 mb-0 font-weight-bold text-gray-800">{{topWords[1]}}</div>
                                        </div>
                                    </div>
                                  
                                </div>
                            </div>
                          </div>
                    </div>
                  <div class="col-xl-3 col-md-3 mb-4">
                        <div class="card border-left-primary shadow h-100 py-2">
                            <div class="card-body">
                                <div class="row no-gutters align-items-center">
                                    <div class="col mr-2">
                                        <div class="text-s font-weight-bold text-primary text-uppercase mb-1" >
                                            Top Keywords</div>
                                        <!-- <div class="h5 mb-0 font-weight-bold text-gray-800">{{this.BurnOutDict["Female"]["Product"]["No"]}}</div> -->
                                        <div>
                                            <div class="h5 mb-0 font-weight-bold text-gray-800">{{topWords[2]}}</div>
                                        </div>
                                    </div>
                                  
                                </div>
                            </div>
                          </div>
                    </div>
              </div>
              <div class = "row mb-2">
                  <div class="col-xl-12 col-md-12 mb-4">
                        <div class="card border-left-primary shadow h-100 py-2">
                            <div class="card-body">
                                <div class="row no-gutters align-items-center">
                                    <div class="col mr-2">
                                        <div class="text-s font-weight-bold text-primary text-uppercase mb-1" >
                                            Analysis Of The Topics</div>
                                        <div>
                                            <div class="h5 mb-0 font-weight-bold text-gray-800" ><p id="analysis"></p></div>
                                        </div>
                                    </div>
                                  
                                </div>
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

</template>
<script>
import axios from "axios";

export default {
  
    data() {
        return {
          burnoutGender:"",
          WFHOptions:"",
          DesignationOption:"",
          resourceOption:"",
          mentalOption:"",
          burnOutValue:"Try Me...",
          classificationResult: "Try Me...",
          classificationText:"",
          topWords:["Loading...","Loading...","Loading..."],
          overallSenti:"Loading...",
        }
    },
    methods:{
      getBurnOutPrediction(){
        if (this.burnoutGender=="" || this.WFHOptions=="" || this.DesignationOption==""|| this.resourceOption==""|| this.mentalOption==""){
          this.burnOutValue= "Error"
        }else{
          axios.post('http://127.0.0.1:5001/getLiveBurnOut',{data:[this.burnoutGender,this.WFHOptions,this.DesignationOption,this.resourceOption,this.mentalOption]})
          .then(res=>{
            console.log(res.data.message)
            this.burnOutValue = res.data.message
          }).catch(err=>{
            console.log(err)
          })
          
        }
      },
       getClassificationResult(){
          //  this.setClassificationResult("Loading...");

          axios.post('http://127.0.0.1:5001/getRealFakeNews',{data:this.classificationText})
            .then(res=>{
              console.log(res.data.message)
              this.classificationResult = res.data.message
            }).catch(err=>{
              console.log(err)
            })
        },
        routeChange(){
      this.$router.push({name: 'Home'});
    },
      
        // async setClassificationResult(result) {
        //   // Use the setTimeout function to delay setting the classificationResult value
        //   await setTimeout(() => {
        //     this.classificationResult = result;
        //   }, 100000); // 1 second delay
        // }

    },
    mounted(){
      axios.post('http://127.0.0.1:5001/getCurrentSentimentAndTopic')
          .then(res=>{
            console.log(res.data.message)
            this.topWords = res.data.message.topWords
            this.overallSenti= res.data.message.overallSenti
            document.getElementById("analysis").innerHTML=res.data.message.analysis
          }).catch(err=>{
            console.log(err)
          })
    }
  }
</script>