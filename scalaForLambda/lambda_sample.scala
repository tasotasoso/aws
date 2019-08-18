package example

import scala.collection.JavaConverters._
import com.amazonaws.services.lambda.runtime.Context
import com.amazonaws.services.lambda.runtime.RequestHandler


trait RepeatBase {
  def repeat(testPhrase: String, context: Context) = {
    println(testPhrase)
  }
}

class Repeat extends RepeatBase