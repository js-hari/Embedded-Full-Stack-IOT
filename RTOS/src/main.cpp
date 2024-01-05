#include <Arduino.h>

#if CONFIG_FREETOS_UNICORE
static const BaseType_t app_cpu = 0;
#else
static const BaseType_t app_cpu = 1;
#endif

/*
static const int led_pin = 1;

void led_blink1(void *parameter)
{
  //run forever
  while(1)
  {
    digitalWrite(led_pin,HIGH);
    Serial.println("led is on");
    vTaskDelay(1000/portTICK_PERIOD_MS);
    digitalWrite(led_pin,LOW);
    Serial.println("led is off");
    vTaskDelay(1000/portTICK_PERIOD_MS);

  }
}
void led_blink2(void *parameter)
{
while(1)
{
digitalWrite(led_pin,HIGH);
Serial.println("Today is friday and still we are having oiur classes .");//cannot d it because it prints all the string at once and due to this we cannt verify that the task is stopped in between or not instead save it as a character array and get ut orinted by taking the single charater using print  such that if the taskstops in bwtween it will be found.the baud rate must be minimum ex 300.
vTaskDelay(1000/portTICK_PERIOD_MS);
digitalWrite(led_pin,LOW);
Serial.println("led2 is off");
vTaskDelay(1000/portTICK_PERIOD_MS);
}
}
void setup() {
  Serial.begin(115200);
  while(!Serial);
  pinMode(led_pin,OUTPUT);

  //create and run the task
  
  
  xTaskCreatePinnedToCore(led_blink1/*function to be called*///"led_blink", /*name os the task*/ 1024/*task satck size*/,//NULL /*parameters to pass to function*/,1 ,/* task priority*/ NULL, /*task handle*/ app_cpu); //run task in one core
 // xTaskCreatePinnedToCore(led_blink2/*function to be called*/,"led_blink", /*name os the task*/ 1024/*task satck size*/,NULL /*parameters to pass to function*/,1 ,/* task priority*/ NULL, /*task handle*/ app_cpu); //run task in one core
//}


//void loop() {
  // code execution will never reach here.
//}

const char msg[] = "Today is friday and still we are attending the classes";

static TaskHandle_t t1 = NULL;
static TaskHandle_t t2 = NULL;


void print_msg(void *parameter)
{
  int len = strlen(msg);
  while(1)
  {
    Serial.println();
    for(int i=0;i<len;i++)
    {
      Serial.print(msg[i]);
      vTaskDelay(10/portTICK_PERIOD_MS);
    }
    Serial.println();
    vTaskDelay(1000/portTICK_PERIOD_MS);
  }
}

void print_star(void *parameter)
{
  while(1)
  {
    Serial.print("*");
    vTaskDelay(100/portTICK_PERIOD_MS);
  }
}

void setup()
{
  Serial.begin(300);
  vTaskDelay(1000/portTICK_PERIOD_MS);
  Serial.println();
  Serial.println("Task Scheduling");
  Serial.println();
  Serial.println("setup and tasks are running in core");
  Serial.println(xPortGetCoreID());
  Serial.println("with priority");
  Serial.println(uxTaskPriorityGet(NULL));

  xTaskCreatePinnedToCore(print_msg,"print msg",1024,NULL,1,&t1,app_cpu);
  xTaskCreatePinnedToCore(print_star,"print star",1024,NULL,2,&t2,app_cpu);

}

void loop()
{
  for(int i = 0;i<4;i++)
  {
    vTaskSuspend(t2);
    vTaskDelay(2000/portTICK_PERIOD_MS);
    vTaskResume(t2);
    vTaskDelay(2000/portTICK_PERIOD_MS);
  }
  if(t1!=NULL)
  {
  vTaskDelete(t1);
  t1=NULL;
  }
}