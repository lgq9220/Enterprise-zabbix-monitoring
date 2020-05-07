package org.hzcitizen.agentpay.filter;

import java.io.IOException;
import java.util.UUID;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServletRequest;

import org.apache.commons.lang3.StringUtils;
import org.hzcitizen.agentpay.util.IPUtils;
import org.slf4j.MDC;
import org.springframework.boot.web.servlet.ServletComponentScan;
import org.springframework.stereotype.Component;

/**
 * Function: 日志输出增加traceid. <br/>
 * Date: 2019年4月10日 下午2:21:52 <br/>
 *
 * @author jianghm
 * @version 1.0
 * @Copyright (c) 2019, 杭州市民卡有限公司  All Rights Reserved.
 */
@Component
@ServletComponentScan
@WebFilter(urlPatterns = "/*",filterName = "logbackFilter")
public class LogbackFilter implements Filter {
	
	private static final String UNIQUE_ID = "traceid";
	private static final String REQ_IP = "merreqip";

	@Override
	public void init(FilterConfig filterConfig) throws ServletException {
		
	}

	@Override
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) {
		HttpServletRequest hsr  = (HttpServletRequest) request;
		String ip = hsr.getHeader("remote_addr");
		if (StringUtils.isEmpty(ip)) {
			ip = IPUtils.getIpAddress(hsr);
		}
		String traceid = hsr.getHeader("traceid");
		boolean flag = insertMDC(traceid, ip);
		try {
			chain.doFilter(request, response);
		}
		catch (IOException | ServletException e) {
		}
		finally {
			if (flag) {
				MDC.remove(UNIQUE_ID);
				MDC.remove(REQ_IP);
			}
		}
	}

	@Override
	public void destroy() {
		
	}
	
	private boolean insertMDC(String traceid, String ip) {
		String uniqueId = null;
		if (StringUtils.isNotEmpty(traceid)) {
			uniqueId = traceid;
		}
		else {
			UUID uuid = UUID.randomUUID();
			uniqueId = uuid.toString().replace("-", "");
		}
        MDC.put(UNIQUE_ID, uniqueId);
        MDC.put(REQ_IP, ip);
		return true;
	}

}

