//necessary inital import for webdriver
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

import org.openqa.selenium.By; //By for finding elements
import org.openqa.selenium.Keys; //For KeyStrokes

//WebDriverWait and Expected Conditions
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;
import java.time.Duration;


public class Selen {
    public static void main(String[] args) {
        System.setProperty("webdriver.gecko.driver", "./geckodriver"); //path to geckodriver (same dir)
        WebDriver driver = new FirefoxDriver(); //driver object

        //get to an web address
        driver.get("https://www.duckduckgo.com");

        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(7));
        wait.until(
            ExpectedConditions.visibilityOfElementLocated(By.className("searchbox_input__rnFzM"))
        );
        var inputElement = driver.findElement(By.className("searchbox_input__rnFzM"));
        inputElement.clear();
        inputElement.sendKeys("Kabeer Shariff Github" + Keys.ENTER);

        wait.until(
            ExpectedConditions.visibilityOfElementLocated(By.partialLinkText("Omar Shariff"))
        );
        
        var link_1 = driver.findElement(By.partialLinkText("Omar Shariff"));
        link_1.click();

        driver.quit();
    }
}
